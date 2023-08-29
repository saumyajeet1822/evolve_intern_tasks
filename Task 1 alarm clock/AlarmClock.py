import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            # Play a sound (Windows only)10
            winsound.Beep(1000, 2000)  # 1000Hz sound for 2 seconds
            break
        time.sleep(1)  # Wait for 1 second before checking the time again

# Get the alarm time from the user
alarm_time = input("Enter the alarm time in HH:MM:SS format: ")

set_alarm(alarm_time)