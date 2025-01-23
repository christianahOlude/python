def interpret_caegory():
	if selection_a > selection_b:
		print("you're EXTROVERTED")
	elif selection_a < selection_b:
		print("you're INTROVERTED")

def get_input(question):
	while True:
		answer = input(question).lower()
		if answer in ['a', 'b']:
			return answer
		else:
			print('Expected A or B')


def main():
	selection_a1 == 0
	#selection_a2 == 0, selection_b2 == 0, 
	
	name = input("What is your name: ")

	questions = ['A. expend energy, enjoy groups '  ' B. conserve energy, enjoy 	one-on-one',
	'A. more outgoing, think out loud '  'B. more reserved, think to yourself'
	'A. seek many tasks,public activities, interaction' ' B. seek 	private,solitary activities with quiet to concentrate'
	'A. external, communicative, express yourself' ' B. internal,reticent, 	keep to yourself'
	'A. active,initiate' ' B. reflective, deliberate']

	for question in questions:
		answer = get_input(question + "\n")
		if answer == 'a':
			selection_a1 += 1
		else:
			selection_b1 += 1

	







def interpret_category():
	if selection_a > selection_b:
		print("you're SENSING")
	elif selection_a < selection_b:
		print("you're INTUITIVE")

def get_input(question):
	while True:
		answer = input(question).lower()
		if answer in ['a', 'b']:
			return answer
		else:
			print('Expected A or B')


def main():
	selection_a1 == 0, selection_b1 == 0, 
	selection_a2 == 0, selection_b2 == 0, 
	

questions = ['A. intepret literally'  'B. look for  meaning and possibilities',
'A. practical, realistic, experimental'  'B. imaginative,innovative, theoretical'
'A. standard, usual, conventional' 'B. differnt, novel, unique'
'A. focus on here-and-now' 'B. look to the future, global perspective, big picture'
'A. facts, things, what is' 'B. ideas, dreams, what could be, philosophical'];

for question in questions:
	answer = get_input(question + "\n")
	if answer == 'a':
		selection_a1 += 1
	else:
		selection_b1 += 1






