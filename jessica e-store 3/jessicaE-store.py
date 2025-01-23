def add_to_cart():
	user_input = view_products()
	print(user_input)

def view_products():
	view = """
	1. Gowns - $1000
	2. Trousers - $500
	3. Tops - $200

"""
	print(view)
	userInput = int(input("Enter a number: "))
	return userInput

def main_menu():
	menu = """
	Welcome to Jessica's E-store
	1. View Products
	2. Add to Cart
	3. Remove from Cart
	4. View Cart
	5. Checkout

	"""
	print(menu)

	answer = int(input("Enter a number: "))

	match(answer):

		case 1 :
			view_products()
		case 2 : 
			add_to_cart()
		#case 3 :
			#remove_from_cart()
		#case 4 : 
			#view_cart()
		#case 5 : 
			#checkout()


main_menu()
add_to_cart()

	