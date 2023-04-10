n = int(input("Please introduce the number of sides of the shape between 3 and 10. \n"))
if n == 3:
    print("The shape is a triangle.")
elif n == 4:
    print("The shape is a square.")
elif n == 5:
    print("The shape is a pentagon.")
elif n == 6:
    print("The shape is a hexagon.") 
elif n == 7:
    print("The shape is a heptagon.")
elif n == 8:
    print("The shape is a octagon.")
elif n == 9:
    print("The shape is a nonagon.")
elif n == 10:
    print("The shape is a decagon.")
else:
    print("You did not introduce a valid number.")