def name_bool(words):
	#return[word == word[: :-1] for word in words]

	return list(map(lambda word : word == word [: :-1], words))