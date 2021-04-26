from pyluach import dates, hebrewcal
from datetime import date

def get_dates(h_year, h_month, h_day, g_date):
    today_hebrew = dates.HebrewDate.today()
    today_greg = today_hebrew.to_pydate()

    if g_date:
        try:
            today_greg = date.fromisoformat(g_date)
            today_hebrew = dates.HebrewDate.from_pydate(today_greg)
        except ValueError:
            raise ValueError(f"{g_date} malformed date.")
    else:
        
        try:
            year, month, day = int(h_year), int(h_month), int(h_day)
            today_hebrew = dates.HebrewDate(year, month, day)
            today_greg = today_hebrew.to_pydate()
        except ValueError:
            raise ValueError(f"{h_day} {h_month}, {h_year} malformed date.")

    return today_hebrew, today_greg
