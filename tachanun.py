import json

data = json.load(open("tachanun_days.json"))

def no_tachanun(month, day):
    month = month.lower().replace("'", "").replace(" ii", "2").replace(" i", "1")
    
    days = data[month]

    for day_dict in days:
        if day >= day_dict["startDay"] and day <= day_dict["endDay"]:
            return day_dict
    
    return False