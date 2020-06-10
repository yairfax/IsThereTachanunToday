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
    month = month_key(date)
    days = data[month]

    for day in days:
        if date.day >= day["startDay"] and date.day <= day["endDay"]:
            return day
    
    if date.day == 30 or date.day == 1:
        return {
            "description": "Rosh Chodesh %s" % month_str_rc(date),
            "source": "Peninei_Halakhah%2C_Prayer.21.7.2",
            "dayBefore": True
        }

    if date.weekday() == 7:
        return {
            "description": "Shabbat Kodesh",
            "source": "Peninei_Halakhah%2C_Prayer.21.7.2",
            "dayBefore": True
        }
    
    return False

def fix_spelling(date_str):
    return date_str.replace("Teves", "Tevet").replace("Iyar", "Iyyar").replace("Nissan", "Nisan").replace("Rishon", "Aleph").replace("Sheni", "Bet")

def month_key(date):    
    return month_str(date).lower().replace(" aleph", "_i").replace(" bet", "_ii")

def month_str(date):
    return fix_spelling(hebrewcal.Month(date.year, date.month).name)

def month_str_rc(date):
    return month_str(date + 1)

def get_hebrew_date_str(date):
    return "%s %s, %s" % (gematria.NumberToGematria(date.day, sofit=False), month_map[month_key(date)], gematria.YearNoToGematria(date.year, sofit=False))