from flask import Flask, render_template, request, jsonify, make_response
from datetime import date
from .tachanun import *
from .dates import *
from .yahrtzeits import *
import requests
from pyluach import dates, hebrewcal
from dataclasses import dataclass
from http import HTTPStatus

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def main(mode=""):
    error = ""
    g_date = request.args.get("g_date")
    h_date = request.args.get("h_date")

    try:
        today_hebrew, today_greg = get_dates(h_date, g_date)
    except ValueError as e:
        today_hebrew = dates.HebrewDate.today()
        today_greg = today_hebrew.to_pydate()
        error = str(e)

    is_tachanun = no_tachanun(today_hebrew, mode=mode)

    return render_template('main.html',
        no_tachanun="mincha" not in is_tachanun if is_tachanun else False,
        date=today_greg.strftime("%a %B %d, %Y"),
        h_day=today_hebrew.day,
        h_month=today_hebrew.month,
        h_year=today_hebrew.year,
        hebrew_date=hebrew_date_english(today_hebrew),
        hebrew_date_hebrew=hebrew_date_hebrew(today_hebrew),
        date_placeholder=today_greg.isoformat(),
        reason=is_tachanun["description_il"] if (mode == "il" and is_tachanun and "description_il" in is_tachanun) else (is_tachanun["description"] if is_tachanun else ""),
        source="http://www.sefaria.org/%s" % is_tachanun["source"] if is_tachanun else "",
        subtitle=is_tachanun["subtitle"] if is_tachanun and "subtitle" in is_tachanun else "",
        mincha="mincha" in is_tachanun if is_tachanun else False,
        error=error,
        mode=mode)

@app.route("/il")
def il():
    return main(mode="il")

@app.route("/pro")
def pro():
    error = ""
    g_date = request.args.get("g_date")
    h_date = request.args.get("h_date")

    try:
        today_hebrew, today_greg = get_dates(h_date, g_date)
    except ValueError as e:
        today_hebrew = dates.HebrewDate.today()
        today_greg = today_hebrew.to_pydate()
        error = str(e)

    is_tachanun = get_yahrtzeit(today_hebrew)

    return render_template('main.html',
        no_tachanun = True,
        date=today_greg.strftime("%a %B %d, %Y"),
        h_day=today_hebrew.day,
        h_month=today_hebrew.month,
        h_year=today_hebrew.year,
        hebrew_date=hebrew_date_english(today_hebrew),
        hebrew_date_hebrew=hebrew_date_hebrew(today_hebrew),
        date_placeholder=today_greg.isoformat(),
        reason=is_tachanun["description"],
        source=is_tachanun["source"],
        mode="pro"
    )

@app.route("/get_months/<int:year>")
def get_months(year):
    return jsonify([fix_spelling(month.name) for month in hebrewcal.Year(year).itermonths()])

@app.route("/get_days/<int:year>-<int:month>")
def get_days(month, year):
    return jsonify(len([i for i in hebrewcal.Month(year, month).iterdates()]))

@app.route("/api")
def api(mode=""):
    g_date = request.args.get("gregorian_date")
    h_date = request.args.get("hebrew_date")

    try:
        today_hebrew, today_greg = get_dates(h_date, g_date)
    except ValueError as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)

    is_tachanun = no_tachanun(today_hebrew, mode=mode)
    
    result = {
        "gregorian_date": str(today_greg),
        "hebrew_date": str(today_hebrew),
        "gregorian_date_friendly": today_greg.strftime("%B %d, %Y"),
        "hebrew_date_friendly": hebrew_date_english(today_hebrew),
        "hebrew_date_hebrew": hebrew_date_hebrew(today_hebrew),
        "tachanun_today": "mincha" in is_tachanun if is_tachanun else True,
        "tachanun_at_mincha": bool(not is_tachanun),
    }

    if is_tachanun:
        result["reason"] = is_tachanun["description_il"] if mode == "il" and "description_il" in is_tachanun else is_tachanun["description"]
        result["source"] = f"https://www.sefaria.org/{is_tachanun['source']}"

        # I hate hardcoding specific cases, but Purim Meshulash is really quite a specific case
        if "subtitle" in is_tachanun and "yerushalaim" in is_tachanun["subtitle"].lower():
            result["extra_info"] = "only in Yerushalaim"

    return jsonify(result)

@app.route("/api/il")
def api_il():
    return api(mode="il")

@app.route("/api/pro")
def api_pro():
    g_date = request.args.get("gregorian_date")
    h_date = request.args.get("hebrew_date")

    try:
        today_hebrew, today_greg = get_dates(h_date, g_date)
    except ValueError as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)

    is_tachanun = get_yahrtzeit(today_hebrew)

    result = {
        "gregorian_date": str(today_greg),
        "hebrew_date": str(today_hebrew),
        "gregorian_date_friendly": today_greg.strftime("%B %d, %Y"),
        "hebrew_date_friendly": hebrew_date_english(today_hebrew),
        "hebrew_date_hebrew": hebrew_date_hebrew(today_hebrew),
        "tachanun_today": False,
        "reason": is_tachanun["description"],
        "source": is_tachanun["source"]
    }

    return jsonify(result)