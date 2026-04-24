from plyer import notification
import time

task = input("Enter task: ")
time_input = input("Enter time: ")

time.sleep(10)

notification.notify(
    title="⏰ Reminder",
    message=f"{task} at {time_input}",
    timeout=10
)