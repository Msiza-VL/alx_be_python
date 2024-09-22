task = input("Enter your task: ").strip()
if not task:
    print("Task cannot be empty. Please provide a valid task.")
    exit()
priority = input("Priority (high/medium/low): ").lower().strip()
if priority not in ["high", "medium", "low"]:
    print("Invalid priority level. Please use high, medium, or low.")
    exit()  
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
if time_bound not in ["yes", "no"]:
    print("Invalid input for time sensitivity. Please answer 'yes' or 'no' .")
exit()
match priority:
   case "high":
      reminder = f"Reminder: '{task}' is a high priority task"
    case "medium"
      reminder = f"Remdinder: '{task}' is a medium priority task"
    case "low":
      reminder = f"Note: '{task}' is a low priority task"
    case  _:
      print("This should never happen due to prior checks.")
      exit()
if time_bound == "yes":
    reminder += " that requires emmediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
print(reminder)