import json
from pyluach import dates, hebrewcal
from dataclasses import dataclass
from dates import *

@dataclass
class TachanunDay:
    tachanun_today: bool
    tachanun_at_mincha: bool
    description: str
    source: str
    subtitle: str

data = json.load(open("tachanun_days.json"))

def no_tachanun(date, recurse=True, mode=""):
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
    
    if mode == "il" and is_purim_meshulash(date):
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