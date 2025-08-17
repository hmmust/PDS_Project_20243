import datetime
import pandas as pd

ts1 = pd.date_range(datetime.datetime.now(),
                         periods=10,freq='D')
ts2 = pd.date_range(datetime.datetime.now(),
                         periods=10,freq='M')
ts3 = pd.date_range(datetime.datetime.now(),
                         periods=10,freq='W')
print(ts3)
