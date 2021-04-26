from flask import Flask, render_template, request, jsonify
from datetime import date
from tachanun import *
from dates import *
import requests
from pyluach import dates, hebrewcal
from dataclasses import dataclass
app = Flask(__name__)

@app.route('/')
def main(il=False):
    error = ""
    try:
        today_hebrew, today_greg = get_dates(
            request.args.get("h_year"),
            request.args.get("h_month"),
            request.args.get("h_day"),
            request.args.get("g_date"))
    except ValueError as e:
        today_hebrew = dates.HebrewDate.today()
        today_greg = today_hebrew.to_pydate()
        error = str(e)

    is_tachanun = no_tachanun(today_hebrew, il=il)

    return render_template('main.html',
        no_tachanun="mincha" not in is_tachanun if is_tachanun else False,
        date=today_greg.strftime("%a %B %d, %Y"),
        h_day=today_hebrew.day,
        h_month=today_hebrew.month,
        h_year=today_hebrew.year,
        hebrew_date="%d %s %d" % (today_hebrew.day, month_str(today_hebrew), today_hebrew.year),
        hebrew_date_hebrew=hebrew_date_str(today_hebrew),
        date_placeholder=today_greg.isoformat(),
        reason=is_tachanun["description_il"] if (il and is_tachanun and "description_il" in is_tachanun) else (is_tachanun["description"] if is_tachanun else ""),
        source="http://www.sefaria.org/%s" % is_tachanun["source"] if is_tachanun else "",
        subtitle=is_tachanun["subtitle"] if is_tachanun and "subtitle" in is_tachanun else "",
        mincha="mincha" in is_tachanun if is_tachanun else False,
        error=error,
        il="il" if il else "")

@app.route("/il")
def il():
    return main(il=True)

@app.route("/get_months/<int:year>")
def get_months(year):
    return jsonify([fix_spelling(month.name) for month in hebrewcal.Year(year).itermonths()])

@app.route("/get_days/<int:year>-<int:month>")
def get_days(month, year):
    return jsonify(len([i for i in hebrewcal.Month(year, month).iterdates()]))

@app.route("/api")
def api(il=False):
    return 