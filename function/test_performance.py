import unittest
from performances import student_names
from performances import student_subjects
from performances import student_scores

class Performances(unittest.TestCase):

	def test_that_student_names_exists(self):
		name = [ayo, afeez, joy]
		result = student_names(name)
		expected_result = ayo, afeez, joy
		self.assertEqual(result, expected_result)

	def test_that_student_subjects_exists(self):
		subject = [java, python, ds, dt]
		result = student_subjects(subject)
		expected_result = java, python, ds, dt
		self.assertedEqual(result, expected_result)

	def test_that_student_scores_exists(self):
		scores = [1 , 100]
		result = student_scores(scores)
		expected_result = 1, 100
		self.assertedEqual(result, expected_result)