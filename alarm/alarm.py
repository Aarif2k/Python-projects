import datetime
from playsound import playsound  #pip install playsound==1.2.2
import time

# Input the alarm time
alarm_Hours = int(input("Hours: "))
alarm_Minutes = int(input("Minutes: "))
am_pm = input("AM / PM: ").strip().lower()

# Convert to 24-hour format
if am_pm == 'pm' and alarm_Hours != 12:
    alarm_Hours += 12
elif am_pm == 'am' and alarm_Hours == 12:
    alarm_Hours = 0

# Continuously check the current time
while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    if alarm_Hours == current_hour and alarm_Minutes == current_minute:
        print("Wake up!")
        playsound('sound-1.mp3')
        break
    
    # Wait for a short period to avoid high CPU usage
    time.sleep(1)
