from flask import Flask, render_template, request
from datetime import date
from tachanun import *
import requests

app = Flask(__name__)

@app.route('/')
def main():
    today = date.today()

    if 'date' in request.args:
        today = today.fromisoformat(request.args.get('date'))

    r = requests.get('https://www.hebcal.com/converter/?cfg=json&gy=%d&gm=%d&gd=%d&g2h=1' % (today.year, today.month, today.day))

    response = r.json()

    tachanun_huh = no_tachanun(response["hm"], response["hd"])
    return render_template('main.jinja',
        no_tachanun=tachanun_huh,
        date=today.strftime("%B %d, %Y"),
        hebrew_date="%d %s %d" % (response["hd"], response["hm"], response["hy"]),
        hebrew_date_hebrew=response["hebrew"],
        date_placeholder=today.isoformat(),
        reason=tachanun_huh["description"] if tachanun_huh else "") 