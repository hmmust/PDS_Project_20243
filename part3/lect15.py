import datetime
t= datetime.datetime.now()
print(t.day)
print(type(t))
#print(datetime.datetime.today())
birthdate = datetime.datetime(2004,2,23)
print(birthdate)
age = t - birthdate
print(age,type(age))