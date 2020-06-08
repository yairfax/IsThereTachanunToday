from flask import Flask, render_template, request
from datetime import date
from tachanun import *
import requests
from pyluach import dates
app = Flask(__name__)

@app.route('/')
def main():
    today_hebrew = dates.HebrewDate.today()
    today_greg = today_hebrew.to_pydate()

    if 'g_date' in request.args:
        today_greg = date.fromisoformat(request.args.get('g_date'))
        today_hebrew = today_hebrew.from_pydate(today_greg)

    tachanun_huh = no_tachanun(today_hebrew)
    return render_template('main.jinja',
        no_tachanun=tachanun_huh,
        date=today_greg.strftime("%B %d, %Y"),
        hebrew_date="%d %s %d" % (today_hebrew.day, month_str(today_hebrew), today_hebrew.year),
        hebrew_date_hebrew=get_hebrew_date_str(today_hebrew),
        date_placeholder=today_greg.isoformat(),
        reason=tachanun_huh["description"] if tachanun_huh else "")