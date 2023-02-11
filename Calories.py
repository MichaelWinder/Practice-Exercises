timeBiking = int(input("How many Hours do you spend Biking? "))
timeJogging = int(input("How many Hours do you spend Jogging? "))
timeSwimming = int(input("How many Hours do you spend Swimming? "))
bikingCal = timeBiking * 200
joggingCal = timeJogging * 475
swimmingCal = timeSwimming * 275
bikingWeight = bikingCal / 3500 * 454
joggingWeight = joggingCal / 3500 * 454
swimmingWeight = swimmingCal / 3500 * 454
totalWeightBurned = (bikingWeight + joggingWeight + swimmingWeight) / 1000
print(f"You have burned {totalWeightBurned:.3f} Kg")
