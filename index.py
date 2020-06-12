from flask import Flask, render_template, request, jsonify
from datetime import date
from tachanun import *
import requests
from pyluach import dates, hebrewcal
app = Flask(__name__)

@app.route('/')
def main(il=False):
    today_hebrew = dates.HebrewDate.today()
    today_greg = today_hebrew.to_pydate()

    if 'g_date' in request.args:
        try:
            today_greg = date.fromisoformat(request.args.get('g_date'))
            today_hebrew = dates.HebrewDate.from_pydate(today_greg)
        except ValueError:
            error = request.args.get('g_date') + " malformed date."
            today_greg = date.today()
            today_hebrew = dates.HebrewDate.today()

    error = ""
    if 'h_day' in request.args:
        year, month, day = int(request.args.get('h_year')), int(request.args.get('h_month')), int(request.args.get('h_day'))
        
        try:
            today_hebrew = dates.HebrewDate(year, month, day)
            today_greg = today_hebrew.to_pydate()
        except ValueError:
            error = "%d %d, %d" % (day, month, year) + " malformed date."
            today_hebrew = dates.HebrewDate.today()
            today_greg = date.today()

    tachanun_huh = no_tachanun(today_hebrew, il=il)

    return render_template('main.html',
        no_tachanun="mincha" not in tachanun_huh if tachanun_huh else False,
        date=today_greg.strftime("%a %B %d, %Y"),
        h_day=today_hebrew.day,
        h_month=today_hebrew.month,
        h_year=today_hebrew.year,
        hebrew_date="%d %s %d" % (today_hebrew.day, month_str(today_hebrew), today_hebrew.year),
        hebrew_date_hebrew=hebrew_date_str(today_hebrew),
        date_placeholder=today_greg.isoformat(),
        reason=tachanun_huh["description_il"] if (il and tachanun_huh and "description_il" in tachanun_huh) else (tachanun_huh["description"] if tachanun_huh else ""),
        source="http://www.sefaria.org/%s" % tachanun_huh["source"] if tachanun_huh else "",
        subtitle=tachanun_huh["subtitle"] if tachanun_huh and "subtitle" in tachanun_huh else "",
        mincha="mincha" in tachanun_huh if tachanun_huh else False,
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