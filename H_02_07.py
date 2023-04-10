print("Please introduce the rating of an employee. \n")
rating = float(input("rating = "))
rs = rating * 2400
if rating == 0.0:
    print("The employee has unacceptable performance.")
    print("The employee will not receive a raise.")
elif rating == 0.4:
    print("The employee has acceptable performance.")
    print("The employee will receive a raise of $1000.")
elif rating >= 0.6:
    print("The employee has meritorious performance.")
    print("The employee will receive a raise of $" + str(rs))
else:
    print("You did not introduce a valid rating.")