import datetime
import pandas as pd

td1 = pd.Timedelta(hours=1, minutes=15)
today_8am = datetime.datetime(2025,8,17,8,0,0)
lectures = pd.date_range(today_8am,periods=5,freq=td1)
print(lectures)

lectures = pd.date_range('8:00','14:00',periods=5)
print(lectures)
