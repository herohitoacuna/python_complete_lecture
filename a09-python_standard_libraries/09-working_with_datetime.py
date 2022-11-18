# ************** WORKING WITH DATETIME ******************
# import datetime
from datetime import datetime, timedelta
import time

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

# strptime("Date format in String", "directives or format"), use to convert DATE STRING into DATE OBJECT
dt3 = datetime.strptime("2018/01/01", "%Y/%m/%d")

# convert the timestamps into time
dt4 = datetime.fromtimestamp(time.time())

print(dt4)           # result: 2022-11-18 18:49:18.561965
print(f"{dt4.year}/{dt4.month}/{dt4.day}")         # result: 2022/11/18

# result: 2022/11/18, strf() method convert DATE STRING into DATE OBJECT
print(dt4.strftime("%Y/%m/%d"))

print(dt2 > dt1)        # result: True


# ************* WORKING WITH TIME DELTA *****************
# Time Delta is also known as "DURATION"

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)                     # 1782 days, 19:27:33.916930
print("days", duration.days)        # result: days 1782
print("seconds", duration.seconds)  # result: seconds 70053
print("total_seconds", duration.total_seconds())
# result: total_seconds 154034941.974594
