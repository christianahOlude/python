tax_bracket = int(input("Enter your annual income: "))	

if(tax_bracket < 9875):
  print("10")
elif (tax_bracket < 40125):
  print("12")
elif(tax_bracket < 85525):
  print("22")
elif (tax_bracket > 85526):
  print("24")