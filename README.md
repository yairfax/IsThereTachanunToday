# Is There Tachanun Today?

For centuries, Jews have asked the same question over and over. _Is there Tachanun today?_ Can I go eat breakfast just a few minutes earlier? Oh and if it's a Monday or a Thursday, there's no greater _simcha_ than not saying tachanun.

I present [IsThereTachanunToday.com](http://istheretachanuntoday.com), a website which answers this question for the _davener_ wondering if he or she can go straight onto Ashrei.

# Installation

To run locally, execute

```bash
pip install -r requirements.txt
export FLASK_APP=index.py
export FLASK_ENV=development
flask run
```

Requires Python 3.7.x

# API

IsThereTachanunToday.com also has an API that can report whether or not there is tachanun.

### `GET /api`

Returns JSON with information on whether there is Tachanun today in Chutz La'aretz. Without any parameters it will return information on the current day.

| Parameter        | Description                                                                                                                        | Format                    | Example                          | Required   |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | -------------------------------- | ---------- |
| `gregorian_date` | The Gregorian date for which to retrieve Tachanun information.                                                                     | `"<year>-<month>-<date>"` | April 28, 2021 is `"2021-04-28"` | _Optional_ |
| `hebrew_date`    | The Hebrew date for which to retrieve Tachanun information. Each value is an integer, and the month value starts with Nissan as 1. | `"<year>-<month>-<date>"` | 16 Iyyar 5781 is `"5781-02-16"`  | _Optional_ |

### `GET /api/il`

Functions the same way as `/api`, but returns information for Israel.
