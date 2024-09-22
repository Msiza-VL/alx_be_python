task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
case "high":
reminder = f"Reminder: '{task}' is a high priority task"
case "medium":
reminder = f"Reminder: '{task}' is a medium priority task"
case "low":
reminder = f"Note: '{task} is a low priority task"
case _:
reminder = "Invalid priority level entered. Please use high, medium, or low."
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
if time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder += " (Time sensitivity input was invalid.)"
print(reminder)