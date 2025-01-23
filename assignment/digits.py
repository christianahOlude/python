num1 = int(input("Enter three digits: "))
 
digit1 = num1 % 10
digit2 = num1 % 100
digit3 = digit2 / 10
digit4 = num1 / 100

sum = digit4 + digit3 + digit1
print(sum)