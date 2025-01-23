user_input = int(input("Enter three digits"))

num1 = user_input % 10
num2 = user_input % 100
num3 = num2 / 10
num4 = num1 / 100

if (num1 == num2):
	print("number is a palindrome")
else: 
	print("number is not a palindrome")