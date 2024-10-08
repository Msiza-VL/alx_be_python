task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
timebound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case :
        reminder = f"'{task}' has an unspecified priority level"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print("Reminder:", reminder)
else:
    reminder += ". Consider completing it when you have free time."
    print("Note:", reminder)