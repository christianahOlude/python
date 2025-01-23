import math

sides = int(input("Enter number of sides: "))
length = int(input("Enter length of one of the sides: "))

area = (sides*length**2) / (4*math.tan(math.pi/sides))
print(area)