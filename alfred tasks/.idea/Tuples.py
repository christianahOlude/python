#Tuples cannot be changed and are created using parentheses
numbers = (1,2,3,4,5,6,7,8,9)
print(numbers)

my_tuple = (1,2,"Esther",[1,4,9])
my_tuple[3][1] = 59
#once strings are defined, it can't be changed
#my_tuple = ("Timothy")
#my_tuple[1] = s
print(my_tuple)

mixed_tuple = (1,"Esther",3.14,[10,20,30],"divine")
mixed_tuple[3][2] = 50
print(mixed_tuple)

#operators
x = (1,3,9)
y = (2,5,8)
print(x + y)
print(x * 3)
print(y * 2)


#tuple methods
numbers = (1,2,3,4,5,4)
numbers.count(3)
numbers.index(4)
print(numbers.count(3))
print(numbers.index(4))

#Tuple membership
#Testing if an item is present in a tuple
the_tuple = ('a','p','p','l','e')
print('l' in the_tuple)
print('w' in the_tuple)
print('p' in the_tuple)

#iterate through a tuple
names = ('Esther','mary','Gloria','John','Kate')
for name in names:
    print('Hello',name)

#method tuple()
mix_tuple = (1,"Esther",3.14,[10,20,30],"divine")
tuple(mix_tuple)
print(mix_tuple)

#method all()
all_tuple = (1,"Esther",3.14,[10,20,30],"divine")
all(all_tuple)
print(all_tuple)

#method any()
any_tuple = (1,"",3.14,[10,20,30],"divine")
any(any_tuple)
print(any_tuple)