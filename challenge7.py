import math

print("enter your first point : ")

x1 = float(input("enter x1 : "))
y1 = float(input("enter y1 : "))

print("enter your second point : ")

x2 = float(input("enter x2 : "))
y2 = float(input("enter y2 : "))


result = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"the distance is {result}")