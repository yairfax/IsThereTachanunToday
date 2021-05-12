# %%
import json
import random
from pkg_resources import resource_filename

data = json.load(open(resource_filename('istheretachanun_app', "resources/yahrtzeits.json")))

# %%
def get_yahrtzeit(h_date):
    month_adj = 12 if h_date.month == 13 else h_date.month
    candidates = data[month_adj - 1][h_date.day - 1]
    choice = random.choice(candidates)
    return {
        "description": f"the yahrtzeit of {choice['name']}",
        "source": f"https://www.breslev.co.il/tzadikim.aspx?category=145&language=english&day={h_date.day}&month={(month_adj % 12) + 6}"
    }
    