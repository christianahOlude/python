
num1 = int(input("Enter five digits: "))

digit1 = num1 / 10000 
digit2 = (num1 / 1000) % 10
digit3 = (num1 / 100) % 10
digit4 = (num1 / 10) % 10
digit5 = num1 % 10



print(digit1,digit2, digit3,digit4,digit5)