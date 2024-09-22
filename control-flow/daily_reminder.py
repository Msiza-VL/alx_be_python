task = input("Enter your task: ").strip()
priority = input("Priority (high/low/medium): ").strip().lower()
time_bound = input("Is it time_bound? (yes/no): ").strip().lower()
if not task or priority not in ['high', 'medium', 'low'] or time_bound not in ['yes', 'no']:
    print("Please provide valid inputs for task, priority, and time-bound status.")
    exit(1) #Exit if input is valid
match prirority:
   case 'high':
      reminder = f"'{task}' is a high priority task"
   case 'medium':
      reminder = f"'{task}' is a medium priority task"
    case 'low':
       reminder = f"'{task}' is a low priority task"
    case _:
       print("Priority not recognized.")
       exit(1)
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
print(reminder)