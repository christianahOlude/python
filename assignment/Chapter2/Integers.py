number1 = int(input('Enter a number: '))
number2 = int(input('Enter a number: '))
number3 = int(input('Enter a number: '))
sum = number1 + number2 + number3
average =number1 + number2 + number3 / 3
product = number1 * number2 * number3

smallest = 0
largest = 0

if number1 > number2 and number1 > number3:
	largest = number1
elif number2 > number3:
	largest = number2
else:
	largest = number3

if number1 < number2 and number1 < number3:
	smallest = number1
elif number2 < number3:
	smallest = number2
else:
	smallest = number3

print(f"average: {average}, sum: {sum}, product: {product}, smallest: {smallest}, largest: {largest} ")