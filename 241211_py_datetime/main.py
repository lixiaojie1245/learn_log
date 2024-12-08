import datetime

print(datetime.datetime.now().strftime("%y%m%d"))


today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow.strftime("%y%m%d"))
