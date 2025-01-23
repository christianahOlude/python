begin = int(input("Enter the value to begin: "))
end = int(input("Enter the end value: "))
number_range = int(input("Enter the range value: "))
count = 0

while begin <= end:
    if begin % 3 == 0:
        count += 1
    begin += 1

print(count)