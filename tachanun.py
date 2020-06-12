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

month_list = ["Nisan", "Iyyar", "Sivan", "Tamuz", "Av", "Elul", "Tisrei", "Cheshvan", "Kislev", "Tevet", "Shvat", "Adar", "Adar Bet"]

data = json.load(open("tachanun_days.json"))

def no_tachanun(date, recurse=True, il=False):
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

    if date.month == 10 and date.day == 3 and hebrewcal.holiday(date) == 'Chanuka': # chanuka if kislev if 29/30 days
        return {
            "description": "Chanukah",
            "source": "Peninei_Halakhah%2C_Prayer.21.7.3",
            "dayBefore": False
        }

    if date.month == 2 and date.day in [3, 4, 5, 6] and is_yom_haatzmaut(date): # yom haatzmaut day of the week
        return {
            "description": "Yom Haatzmaut",
            "source": "Peninei_Halakhah%2C_Prayer.21.7.4",
            "dayBefore": True
        }

    if date.month == 5 and date.day in [9, 10] and hebrewcal.holiday(date) == "9 of Av": # nidcheh tisha b'av
        return {
            "description": "Tisha B'Av",
            "source": "Peninei_Halakhah%2C_Prayer.21.7.3",
            "dayBefore": True
        }
    
    if il and is_purim_meshulash(date):
        return {
            "description": "Purim Meshulash",
            "source": "Peninei_Halakhah%2C_Prayer.21.7.3",
            "dayBefore": False,
            "subtitle": "...only in Yerushalaim!"
        }

    if recurse:
        tomorrow = no_tachanun(date + 1, recurse=False)
        if tomorrow and tomorrow["dayBefore"]:
            return {
                "mincha": True,
                "subtitle": "...but there's no Tachanun at Mincha!",
                "description": tomorrow["description"],
                "source": "Peninei_Halakhah%2C_Prayer.21.7.3"
            }

    return False

def yom_haatzmaut(year):
    hey_iyyar = dates.HebrewDate(year, 2, 5)
    d_of_week = hey_iyyar.weekday()

    if d_of_week == 4:
        return hey_iyyar

    elif d_of_week == 6:
        return dates.HebrewDate(year, 2, 4)

    elif d_of_week == 7:
        return dates.HebrewDate(year, 2, 3)

    elif d_of_week == 2:
        return dates.HebrewDate(year, 2, 6)

def is_yom_haatzmaut(date):
    return date == yom_haatzmaut(date.year)

def is_purim_meshulash(date):
    month = 13 if hebrewcal.Year(date.year).leap else 12

    return date.month == month and date.day == 16 and date.weekday() == 1

def fix_spelling(date_str):
    return date_str.replace("Teves", "Tevet").replace("Iyar", "Iyyar").replace("Nissan", "Nisan").replace("Rishon", "Aleph").replace("Sheni", "Bet")

def month_key(date):    
    return month_str(date).lower().replace(" aleph", "_i").replace(" bet", "_ii")

def month_str(date):
    return fix_spelling(hebrewcal.Month(date.year, date.month).name)

def month_str_rc(date):
    return month_str(date + 1)

def hebrew_date_str(date):
    return "%s %s, %s" % (gematria.NumberToGematria(date.day, sofit=False), month_map[month_key(date)], gematria.YearNoToGematria(date.year, sofit=False))
