def divide_or_square(number):
	EXPONENTIAL = 0.5
	if number < 0:
		raise ValueError('must be positive')
	if number == "fareedat":
		raise TypeError('must be number')
	if number == " ":
		raise TypeError('must input number')
	if number == "hdhjh":
		raise TypeError('must input number')
	if number % 5 == 0:
		return f"{number ** EXPONENTIAL:.2f}"

	else: 
		return number % 5




print(divide_or_square(40))

	
	