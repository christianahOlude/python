weight_in_pounds = float(input("Enter weight_in_pounds: "))
height_in_inches = float(input("Enter height_in_inches: "))

weight_in_kilogram = weight_in_pounds * 0.45359237
height_in_meters = height_in_inches * 0.0254

bmi = weight_in_kilogram / (height_in_meters * height_in_meters)

print(bmi)

