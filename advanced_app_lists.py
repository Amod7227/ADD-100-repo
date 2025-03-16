# Create list with time slots available
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Empty list for bpm
heart_rate = []

# Empty list for user's name
user_name = []

# Input for user name
user_name = input("What is your name?: ")
# For loop to collect data
for time in time_slots:
    bpm = int(input(f"What is your hear rate (BPM) for the {time} time slot: "))
    #Multi-level list for time slot and bpm input
    heart_rate.append([time, bpm])  

# Heart rate average
average_bpm = sum(rate[1] for rate in heart_rate) / len(heart_rate)
round(average_bpm)
# Print results of data
print("\nHeart rate data:")
for time, bpm in heart_rate:
    print(f"{time}: {bpm} BPM")

# Print average bpm for the day
print(f"{user_name}, your average heart rate is: {average_bpm} BPM")