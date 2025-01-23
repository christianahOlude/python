negative = 0
positive = 0
zero = 0

for counter in range(5):
	number = int(input("Enter a number: "))

	if number < 0:
	    	negative += 1
	elif number == 0:
		zero += 1
	else: 
	  	positive += 1

print(f"negative {negative}, positive {positive}, zero {zero}")


