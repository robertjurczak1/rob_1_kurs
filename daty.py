import time
from datetime import date, datetime #z biblioteki co
import calendar as cal # import całej biblioteki
import arrow

today = date.today ()
print(today)
print(today.ctime())
print(today.isoformat())

print(today.weekday())
print(cal.calendar(1895))
print(cal.day_name[today.weekday()])
print("Mamy dziś", today.day, "w roku", today.year)

day_of_year = today.timetuple().tm_yday

print("Dziś jest", day_of_year, "dzień roku")
print(today.timetuple())

print(time.ctime())
print(time.gmtime())
print(time.localtime())
print(time.time())

now = datetime.now()
print(now)

print(arrow.utcnow())

local = arrow.now("Europe/Warsaw")
print(local)
print(local.to("Europe/Rome"))
print(local.to("Asia/Tokyo"))
