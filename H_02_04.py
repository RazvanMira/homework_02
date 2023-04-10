month = input("Please introduce the name of a month.\n")
days_30 = ["April", "June", "September", "November"]
days_31 = ["January", "March", "May", "July", "August", "October", "December"]
if month in days_30:
    print("The month of", month, "has 30 days.")
elif month in days_31:
    print("The month of", month, "has 31 days.")
elif month == "February":
    print("The month of February has 28 or 29 days.")