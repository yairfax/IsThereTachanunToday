from flask import Flask, render_template, request, jsonify
from datetime import date
from tachanun import *
import requests
from pyluach import dates, hebrewcal
app = Flask(__name__)

@app.route('/')
def main():
    today_hebrew = dates.HebrewDate.today()
    today_greg = today_hebrew.to_pydate()

    if 'g_date' in request.args:
        today_greg = date.fromisoformat(request.args.get('g_date'))
        today_hebrew = dates.HebrewDate.from_pydate(today_greg)

    error = ""
    if 'h_day' in request.args:
        year, month, day = int(request.args.get('h_year')), int(request.args.get('h_month')), int(request.args.get('h_day'))
        
        try:
            today_hebrew = dates.HebrewDate(year, month, day)
        except ValueError:
            error = "%d %s %d" % (day, month_list[month - 1], year) + " doesn't exist"
            day = 29
            today_hebrew = dates.HebrewDate(year, month, day)
        today_greg = today_hebrew.to_pydate()

    tachanun_huh = no_tachanun(today_hebrew)
    return render_template('main.html',
        no_tachanun="mincha" not in tachanun_huh if tachanun_huh else False,
        date=today_greg.strftime("%B %d, %Y"),
        h_day=today_hebrew.day,
        h_month=today_hebrew.month,
        h_year=today_hebrew.year,
        hebrew_date="%d %s %d" % (today_hebrew.day, month_str(today_hebrew), today_hebrew.year),
        hebrew_date_hebrew=hebrew_date_str(today_hebrew),
        date_placeholder=today_greg.isoformat(),
        reason=tachanun_huh["description"] if tachanun_huh else "",
        source="http://www.sefaria.org/%s" % tachanun_huh["source"] if tachanun_huh else "",
        subtitle=tachanun_huh["subtitle"] if tachanun_huh and "subtitle" in tachanun_huh else "",
        mincha="mincha" in tachanun_huh if tachanun_huh else False,
        error=error)

@app.route("/get_months/<int:year>")
def get_months(year):
    return jsonify([fix_spelling(month.name) for month in hebrewcal.Year(year).itermonths()])