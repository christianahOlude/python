def get_student_info():
	name = input('Enter a name: ')
	subjects = []
	for i in range(4):
		subject = input('Enter a subject: ')
		subjects.append(subject)
	return name, subject

def get_scores(subjects):
	scores = {}
	for subject in subjects:
		while True:
			try:
				score = float(input('enter score: '))
				if score > 0 and score <= 100 :
					scores[subject] = score
					break
				else:
					print('score must  be btw 0 & 100')
			except ValueError:
				print('must be a number')
		return scores
				
				
	
	

	


name, subjects = get_student_info()
scores = get_scores(subjects)
print(name, scores)





	