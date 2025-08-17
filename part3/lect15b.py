import datetime
import pandas as pd

#td1 = pd.Timedelta("1 hour 15 minutes")
td1 = pd.Timedelta(hours=1, minutes=15)
#td1 = pd.Timedelta(75,unit='minutes')
today_8am = datetime.datetime(2025,8,17,8,0,0)
print(td1, type(td1))
print(today_8am+td1)
print(today_8am-td1)