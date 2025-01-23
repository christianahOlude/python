my_dict = {"name": "Alice", "age":25, "city": "New York"}
print(my_dict)

#print a key
print(my_dict["name"])

#if statement
if "city" in my_dict:
	print("City is in my dictionary.")

#delete
del my_dict["city"]
print(my_dict)

#replace
my_dict["city"] = "lagos"
print(my_dict["city"])

#to get a value using get()sss
print(my_dict.get("name"))
print(my_dict.get("salary"))
print(my_dict.get("salary","Not Availabe"))

#iterate through the keys
for key in my_dict:
	print(key)

#iterate through values using a method
for values in my_dict.values():
	print(values)

#iterate through key-values pairs
for key,values in my_dict.items():
	print(f"{key}: {values}")

#dictionary comprehension
squared =  {x:x**2 for x in range(1,6)}
print(squared)

even = {x:x**2 for x in range(1, 10 +1)if x % 2 == 0}
print(even)
#int
my_dict = {1:1, 2:4, 3:9, 4:16}
print(my_dict)

