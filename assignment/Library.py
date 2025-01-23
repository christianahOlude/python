number_of_days = int(input("Enter number of days: "))
if (number_of_days <= 5):
	print("your fine is 50 paise")
elif (number_of_days <= 10):
	print("your fine is one rupee")
elif (number_of_days <= 29):
	print("your fine is 5 rupees")
elif (number_of_days > 30):
	print("your membership is cancelled")
