number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))
number4 = int(input("Enter a number: "))

sum = number1 + number2 + number3 + number4
average = number1 + number2 + number3 + number4 / 4
product = number1 * number2 * number3 * number4

largest = 0
smallest = 0
 
if (number1 > number2 and number1 > number3 and number1 > number4):
  print("number1 is the largest number")

elif (number2 > number3 and number2 and number4):
  print("number2 is the largest number")

elif (number3 > number4):
  print("number3 is the largest number")
else:
  print("number4 is the largest number")


if (number1 < number2 and number1 < number3 and number1 < number4):
  print("number1 is the smallest number")

elif (number2 < number3 and number2 < number4):
  print("number2 is the smallest number")

elif (number3 < number4):
  print("number3 is the smallest number")
else:
  print("number4 is the smallest number")


print(f"sum {sum}, average {average}, product {product}")
