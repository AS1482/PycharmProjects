from pandas import DataFrame
from datetime import datetime as dt, timedelta

def to_iso_dict(data):
    if isinstance(data, DataFrame):
        return to_iso_dict(data.to_dict)
    if isinstance(data, dict):
        return {to_iso_dict(key):to_iso_dict(value) for key, value in data.iteritems()}
    if isinstance(data, list):
        return [to_iso_dict(v) for v in data]



df = DataFrame()

date = dt(2010, 12, 01)
end = dt(2016, 12, 30)
step = timedelta(days=5)

holidays = []

while date < end:
    holidays.append(dt)
    date += step


print holidays
data = {'Holidays' : holidays}

df_data = DataFrame(data=data)

print df_data

result = {'ticker':{'field':df_data}}

df_result = DataFrame(result)

print df_result



to_dict = df_result.to_dict()

print to_dict



