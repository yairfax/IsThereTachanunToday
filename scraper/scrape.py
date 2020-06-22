from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from pyluach import hebrewcal
from datetime import date
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import json
from traceback import print_exc

regex = re.compile(r"\((\d{4})(\/(\d{4}))?\)\.")

def scrape_day(month, day):
    r = requests.get("https://www.breslev.co.il/tzadikim.aspx?category=145&language=english&day=%d&month=%d" % (day, month))

    soup = BeautifulSoup(r.content, features="lxml")

    big_table = soup.find("table", id="ContentPlaceHolderBase_ContentPlaceHolder1_dlTzadikim")

    all_tables = big_table.find_all("tr", recursive=False) if big_table else []

    return list(map(scrape_row, all_tables))

def get_year(text):
    years = regex.findall(text)
    if not years:
        return None, None, text
    
    years = years[0]
    if not years[1]:
        return int(years[0]), None, regex.sub("", text).strip()

    return int(years[2]), int(years[0]), regex.sub("", text).strip()

def scrape_row(row):
    tables = row.find_all("table")
    description_text = tables[1].find("table").find_all("tr", recursive=False)[1].find_all("td")[2].text.rstrip("\n")
    g_year, h_year, description = get_year(tables[1].find("table").find_all("tr", recursive=False)[1].find_all("td")[2].text.rstrip("\n"))
    return {
        "name": tables[0].findAll("td")[1].text,
        "description": description,
        "g_year": g_year,
        "h_year": h_year
    }

if __name__ == "__main__":
    results = [[None for i in range(30)] for j in range(12)]
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(scrape_day, month + 1, day + 1): (month, day) for month in range(12) for day in range(30)}

        for future in tqdm(as_completed(futures), total=len(futures)):
            month, day = futures[future]
            result = future.result()
            results[(month + 6) % 12][day] = result

    json.dump(results, open("yahrtzeits.json", "w"))