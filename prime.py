def is_prime(num):
    if num < 2:
	return "number must be greater than 1"
    
    for value in range(2,num):
	if num % value == 0:
		find_out = num % value
		print ("Abefore False". find_out)
		return False
		print("After False". find_out)
    return True



number = int(input("slot in a number: ")

print(is_prime(number))
