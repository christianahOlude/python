first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))

sum = first_number + second_number + third_number
print(sum)

average = sum / 3
print(average)

product = first_number * second_number * third_number
print(product)

if first_number > second_number and first_number > third_number:
     print("this is the largest",first_number)
if second_number > first_number and second_number > third_number:
     print("this is the largest",second_number)
if third_number > first_number and third_number > second_number:
    print("this is the largest",third_number)

 
if first_number < second_number and first_number < third_number:
     print("this is the smallest",first_number)
if second_number < first_number and second_number < third_number:
     print("this is the smallest",second_number)
if third_number < first_number and third_number < second_number:
     print("this is the smallest",third_number)