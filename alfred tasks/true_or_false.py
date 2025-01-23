def true_or_false(numbers):
	result = []
	for number in numbers:
		if number % 2 == 0:
			result.append(True)
		else:
			result.append(False)
	return result