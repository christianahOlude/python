def alphanum(name):
	#return[int(letter) for letter in name if letter.isdigit()/isnumber()]

	return list(map(lambda x: int(x),filter(lambda x:x. isdigit(), name)))