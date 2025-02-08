def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


# Example usage
text = "Hello, World!"
shift = 4
encrypted_text = encrypt(text, shift)
print("Encrypted Text: ", encrypted_text)

text = input("Enter the text: ")
shift = int(input("Enter the shift: "))




