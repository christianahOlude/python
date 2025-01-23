def my_dict_in_zip(keys, values):
	my_dict = {}

	for key,value in zip(keys,values):
		my_dict[key] = value
	print(my_dict_in_zip(keys, values))