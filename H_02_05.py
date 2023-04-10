print("Please introduce the lengths of the three sides.")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == b and a == c:
    print("The triangle is equilateral.")
elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print("The triangle is isosceles.")
elif a != b and b != c and a != c:
    print("The triangle is scalene.")