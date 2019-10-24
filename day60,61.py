import re
import json
week  = {
   "day1": "sunday",
    "day2":"monday",
   "day3": "tuesday",
   "day4": "wednesday",
   "day5": "thursday",
    "day6":"friday",
   "day7": "saturday"
}

print(type(week))

x=json.dumps(week)
print(x)


#__________________________________


str = "date is the new oil"
x=re.findall("date",str)
print(x)