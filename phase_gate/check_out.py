import datetime 
 
def get_discount(total): 
	discount = float(input("Enter discount (%): ")) 
	return total * (discount / 100) 
def invoice(cashier_name, customer_name, date, items_list, total, discount, vat, bill_total): 
	print("====================================") 
	print("SEMICOLON STORE\nMAIN BRANCH\nLOCATION: 312 SEMICOLON WAY.\nTEL: 000000") 
	print(f"CASHIER: {cashier_name}\nCUSTOMER NAME: {customer_name}\nDATE: {date}")
	print("====================================") 
	print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")
	for item in items_list: 
		print_message(item) 
	print("-------------------------------------------") 
	print(f"SUBTOTAL: {total:.2f}")(f"DISCOUNT: {discount:.2f}") 
	print(f"VAT: {vat:.2f}") 
	print_message("-------------------------------------------") 
	print(f"BILL TOTAL: {bill_total:.2f}") 
	print("============================================") 
	print(f"THIS IS NOT A RECEIPT {bill_total:.2f}") 
def receipt(cashier_name, customer_name, date, items_list, total, discount, vat, bill_total, amount_paid): 
	print("====================================") 
	print("SEMICOLON STORE\nMAIN BRANCH\nLOCATION: 312 SEMICOLON WAY.\nTEL: 03") 
	print(f"CASHIER: {cashier_name}\nCUSTOMER NAME: {customer_name}\nDATE: {date}") 
	print("====================================") 
	print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)") 

	for item in items_list: print_message(item) 
	print("-------------------------------------------") 
	print(f"SUBTOTAL: {total:.2f}") 
	print(f"DISCOUNT: {discount:.2f}") 
	print(f"VAT: {vat:.2f}") 
	print("-------------------------------------------") 
	print(f"BILL TOTAL: {bill_total:.2f}") 
	print(f"AMOUNT PAID: {amount_paid:.2f}") 
	print(f"BALANCE: {amount_paid - bill_total:.2f}") 
	print("============================================") 
	print("THANK YOU FOR YOUR PATRONAGE") 
	print("============================================") 
def main():
	date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
	customer_name = input_data() 
	print("Customer name: ") 
	cashier_name = input_data()
	print("Cashier name: ")
 
	items_list = [] 
	total = 0.0 
	VAT_RATE = 17.50 / 100
 
	while True: 
		items = input("What do you want to buy: ") 
	
		pieces =("How many pcs: ") 

		price = ("Price per piece: ") 
	
		item_total = pieces * price 

		total += item_total
 
		items_list.append(f"\t{items}\t{pieces:.2f}\t{price:.2f}\t{item_total:.2f}") 

		user_input = ("Do you want to buy something else? (yes/no): ") 
		if user_input.lower() != 'yes': break 

		discount = get_discount(total) 
		vat = VAT_RATE * total 
		bill_total = (total - discount) + vat 

		invoice(cashier_name, customer_name, date, items_list, total, discount, vat, bill_total) 
		amount_paid = ("How much did the customer give to you: ") 

	receipt(cashier_name, customer_name, date, items_list, total, discount, vat, bill_total, amount_paid)