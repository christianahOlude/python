number_of_pass = 0
number_of_fail = 0


for count in range(1, 16):
   scores = int(input(f"Enter number {count} : "))

   if scores >= 45:
      number_of_pass += 1
   else:
      number_of_fail +=1
	 
	

print(f"{number_of_pass} pass,{number_of_fail} fail")
