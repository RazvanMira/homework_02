print("Please introduce the month and day. \n")
month = input("The month is ")
day = int(input("The day is "))
if month == "January" or month == "February":
    print("It is winter.")
elif (month == "December" and day >= 21) or (month == "March" and day < 20):
    print("It is winter.")
elif month == "April" or month == "May":
    print("It is spring.")
elif (month == "March" and day >= 20) or (month == "June" and day < 21):
    print("It is spring.")
elif month == "July" or month == "August":
    print("It is summer.")
elif (month == "June" and day >= 21) or (month == "September" and day < 22):
    print("It is summer.")
elif month == "October" or month == "November": 
    print("It is fall.")
elif (month == "September" and day >= 22) or (month == "December" and day < 21):
    print("It is fall.")
