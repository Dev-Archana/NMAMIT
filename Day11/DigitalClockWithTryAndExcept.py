import time
import datetime
import os

try:
    while True:
        now = datetime.datetime.now()
        time_string = now.strftime("%H:%M:%S")
        date_string = now.strftime("%A, %d %B %Y")

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for each update
        print("🕒 Digital Clock\n")
        print("Time:", time_string)
        print("Date:", date_string)

        time.sleep(1)  # Update every 1 second
except KeyboardInterrupt:
    print("\nClock stopped.")
