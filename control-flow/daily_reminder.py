task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time_bound? (yes/no): ").lower()
match priority:
  case 'high':
reminder = f"'{task}' is a high priority task"
if time_bound == 'yes':
reminder += " that requires immediate attention today!"
case 'medium':
reminder = f"'{task}' is a medium priority task."
if time_bound == 'yes':
reminder += "Make sure to address it soon!"
case 'low':
reminder = f"'{task}' is a low priority task."
if time_bound == 'yes':
reminder += "You might want to complete it when you can."
case _:
reminder = "Invalid priority level."
if reminder:
    print(reminder)