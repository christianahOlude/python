<<<<<<< HEAD
 def encrypt(message: str,key:int):
=======
def encrypt(message: str,key:int):
>>>>>>> 01d7e5c98b09478aedaa39fd2aab8df4fb911103
	encrypted = ""
	for letter in message:
		if letter == "":
			encrypted += "#"
		elif letter == letter.lower() and letter != "":
			index = alphabets.index(letter)
			number = index + key
			encrypted +=alphabets[number]

		elif letter == letter.upper():
			index = alphabets2.index(letter)
			number = index + key
			encrypted += alphabets2[number]
	return encrypted

def decrypt(encrypted, key):
	decrypted = ""
	for letter in encrypted:
		if letter == "#":
			decrypted += ""
		elif letter == letter.lower() and letter != "":
			index = alphabets.index(letter)
			number = index - key
			decrypted += alphabets[number]

		elif letter == letter.upper():
			index = alphabets2.index(letter)
			number = index - key
			decrypted += alphabets2[number]
	return decrypted


message = input("Enter message to be encrypted: ")
key = int(input("Enter a key: "))



alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets2 = "ABCDEFGHIJKLNOPQRSTUVWXYZ" 

print(encrypt)
print(decrypt)
