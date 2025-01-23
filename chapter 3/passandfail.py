passes = 0

for numbers in range(10):

  while True:
    result = int(input("Enter result (1 for pass and 2 for fail): "))
   
if result == 1:
   print("passed")
   passes = passes + 1
   break 
elif result == 2:
   print("failed") 
   break
else:
   print("incorrect input, try again")

print("passed: ", passed)
print("failed: ", failed)

if passes > 8:
   print("Bonus to the teacher")