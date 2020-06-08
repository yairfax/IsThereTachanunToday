import json
from pyluach import dates, hebrewcal
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
data = json.load(open("tachanun_days.json"))

def no_tachanun(date):
    month = get_key(date)
    days = data[month]

    for day in days:
        if date.day >= day["startDay"] and date.day <= day["endDay"]:
            return day
    
    return False

def fix_spelling(date_str):
    return date_str.replace("Teves", "Tevet").replace("Iyar", "Iyyar").replace("Nissan", "Nisan").replace("Rishon", "Aleph").replace("Sheni", "Bet")

def get_key(date):    
    return month_str(date).lower().replace("aleph", "_i").replace("bet", "_ii")

def month_str(date):
    return fix_spelling(hebrewcal.Month(date.year, date.month).name)

def get_hebrew_date_str(date):
    return "%s %s, %s" % (gematria.NumberToGematria(date.day), month_map[get_key(date)], gematria.YearNoToGematria(date.year, sofit=False))