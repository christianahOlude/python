integer = int(input("Enter an integer number: "))
convert_binary = " "

while integer > 0:
    remaining = integer % 2
    convert_binary = str(remaining) + convert_binary
    integer = integer // 2

print(convert_binary)