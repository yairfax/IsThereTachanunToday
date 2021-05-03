from pyluach import dates, hebrewcal
from datetime import date
from njdate import gematria

month_map = {
    "tishrei": "תשרי",
    "cheshvan": "חשוון",
    "kislev": "כסלו",
    "tevet": "טבת",
    "shvat": "שבט",
    "adar": "אדר",
    "nisan": "ניסן",
    "iyyar": "אייר",
    "sivan": "סיון",
    "tamuz": "טמוז",
    "av": "אב",
    "elul": "אלול",
    "adar_i": "אדר א׳",
    "adar_ii": "אדר ב׳"
}

month_list = ["Nisan", "Iyyar", "Sivan", "Tamuz", "Av", "Elul", "Tisrei", "Cheshvan", "Kislev", "Tevet", "Shvat", "Adar", "Adar Bet"]

def get_dates(h_date, g_date):
    today_hebrew = dates.HebrewDate.today()
    today_greg = today_hebrew.to_pydate()

    if g_date:
        try:
            today_greg = date.fromisoformat(g_date)
            today_hebrew = dates.HebrewDate.from_pydate(today_greg)
        except ValueError:
            raise ValueError(f"{g_date} malformed date.")
    elif h_date:
        try:
            today_hebrew = parse_h_date(h_date)
            today_greg = today_hebrew.to_pydate()
        except ValueError:
            raise ValueError(f"{h_date} malformed date.")

    return today_hebrew, today_greg

def parse_h_date(h_date):
    year, month, day = [int(val) for val in h_date.split("-")]

    return dates.HebrewDate(year, month, day)

def fix_spelling(date_str):
    return date_str.replace("Teves", "Tevet").replace("Iyar", "Iyyar").replace("Nissan", "Nisan").replace("Rishon", "Aleph").replace("Sheni", "Bet")

def month_key(date):    
    return month_str(date).lower().replace(" aleph", "_i").replace(" bet", "_ii")

def month_str(date):
    return fix_spelling(hebrewcal.Month(date.year, date.month).name)

def month_str_rc(date):
    return month_str(date + 1)

def hebrew_date_hebrew(date):
    return f"{gematria.NumberToGematria(date.day, sofit=False)} {month_map[month_key(date)]}, {gematria.YearNoToGematria(date.year, sofit=False)}"

def hebrew_date_english(h_date):
    return f"{h_date.day} {month_str(h_date)} {h_date.year}"