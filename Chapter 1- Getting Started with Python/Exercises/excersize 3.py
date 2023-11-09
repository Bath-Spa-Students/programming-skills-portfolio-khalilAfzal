#This is the import date and time which allowes the software to extract the exact time
import datetime
now = datetime.datetime.now()
#Then we print what we enter
print("Current date and time")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


