from datetime import date, time,datetime


#  making the instances of datetime
date1 = date(year=2020,month=5,day=25)
# print(date1)

time1 = time(hour=13,minute=25,second=48)
# print(time1)

datetime1 = datetime(year=2020,month=5,day=17,hour=15,minute=11,second=58)
# print(datetime1)

date2 = date.today()
# print(date2)
now1 = datetime.now()
# print(now1)

datetime2 = datetime.combine(date2,time(now1.hour,now1.minute,now1.second))
# print(datetime2)

date3 = date.fromisoformat("2025-01-31")
# print(date3)

date_string = "01-31-2020 14:45:37"
format_string = "%m-%d-%Y %H:%M:%S"
date4 = datetime.strptime(date_string,format_string)
# print(date4)




