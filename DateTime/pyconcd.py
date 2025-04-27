# Creating a countdown timer.
from dateutil import tz
from datetime import  datetime,timedelta

now1 = datetime.now(tz=tz.tzlocal())
# print(now1)

London_tz = tz.gettz("Europe/London")
now2 = datetime.now(tz=London_tz)

#  Improving Countdown Timer

PYCON_DATE = datetime(year=2025,month=5,day=14,hour=9)
# print(pycon_date)

countdown = PYCON_DATE - datetime.now()
# print(countdown)

now5 = datetime.now()
# print(now5)

tomorrow = timedelta(days=+1)
# print(now5+tomorrow)
delta = timedelta(days=+3, hours=-4)
print(now5 + delta)

