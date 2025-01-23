
number = int(input('enter a number from 100 to 999'))
last = number % 10
second  = (number % 100) // 10
first  = number // 100
print(last, second, first)

Even = 0
Odd = 0

if first % 2 == 0:
  Even += 1
else: Odd += 1

if second % 2 == 0:
  Even += 1
else: Odd += 1

if last % 2 == 0:
  Even += 1
else: Odd += 1

print(Even, Odd)