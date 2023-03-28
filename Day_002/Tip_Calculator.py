print("Welcome to the tip calculator.")
bill=input("What was the total bill? " + "$")
bill=int(bill)
people=input("How many people to split the bill? ")
people=int(people)
tip=(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip=float(tip)
if tip==10:
    print("Each person should pay: $" + str((tip/100*bill)/people))
elif tip==12:
    print("Each person should pay: $" + str((tip/100*bill)/people))
elif tip==12:
    print("Each person should pay: $" + str((tip/100*bill)/people))
else:
    print("The tip was not selected from the list.")