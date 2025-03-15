#List containing days of the week
Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Empty list for steps counter
Steps =[]

#User input to provide # of steps for each day
for day in Days:
    while True:
        try:
            user_input = int(input(f"How many steps did you take on {day}: "))
            Steps.append(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


# Display of daily steps
for i in range(len(Days)):
    print(f"On {Days[i]} ,you walked {Steps[i]} steps.")

# Total # of steps in week
total_steps = sum(Steps)
print(f"\nYou had {total_steps} steps taken this week.")

# Average steps per day
average_steps = total_steps / len(Days)
print(f"You averaged {average_steps:.2f} steps this week. Keep it up!")