import multiprocessing
import sys
import os
sys.path.append('../Alpha_One')
from src.package import Subject


class Evaluator:
	"""
	Evaluator class
	"""
	
	def __init__(self):
		from config.config import subject_dictionary
		self.subject_dict = subject_dictionary
		self.current_best = 0
	
	def evaluate_process(self, final_schedules, best_schedules, input_schedule_score, better_than_input_schedules):
		"""
		Evaluates generated schedules and updates the best schedules list.

		:param final_schedules: A list of generated schedules.
		:param best_schedules: A list containing the best schedules found.
		:param input_schedule_score: The score of the input schedule.
		:param better_than_input_schedules: A list of schedules with scores better than the input schedule.
		:return: None
		"""
		if not isinstance(final_schedules, multiprocessing.managers.ListProxy):
			raise TypeError("Final schedules has to be listproxy")
		
		if not isinstance(best_schedules, multiprocessing.managers.ListProxy):
			raise TypeError("Best schedules has to be listproxy")
		
		if not isinstance(input_schedule_score, int):
			raise TypeError("Input schedule score has to be int")
		
		if not isinstance(better_than_input_schedules, multiprocessing.managers.ListProxy):
			raise TypeError("Better than input schedules has to be listproxy")
		
		while True:
			try:
				week = final_schedules.pop()
				score = self.evaluate(week)
				if score > self.current_best:
					self.current_best = score
					week.append(score)
					best_schedules.append(week)
				if score > input_schedule_score:
					better_than_input_schedules.append(week)
			except Exception as e:
				pass
	
	def evaluate(self, week):
		"""
		Evaluates a school schedule and assigns a score based on predefined rules.
		
		RULE 8: if day contains Math and right after id AM => that's bad and in reverse AM->M is also bad
		
		RULE 9: if first subject at the morning is PE => that's bad

		:param week: A list representing a week's schedule.
		:return: The score of the evaluated schedule.
		"""
		if not isinstance(week, list):
			raise TypeError("Week has to be list, []")
		
		if not all(isinstance(subject, int) for subject in week):
			raise ValueError("Subject has to be represented as int")
		
		monday = week[0:10]
		tuesday = week[10:20]
		wednesday = week[20:30]
		thursday = week[30:40]
		friday = week[40:50]
		
		score = 0
		# RULE 2
		ordinary_subjects = [11, 12, 13, 15, 16]
		for subject in ordinary_subjects:
			if monday.count(subject) > 1:
				score -= 23
			if tuesday.count(subject) > 1:
				score -= 23
			if wednesday.count(subject) > 1:
				score -= 23
			if thursday.count(subject) > 1:
				score -= 23
			if friday.count(subject) > 1:
				score -= 23
		
		subjects_hate = ["AM", "CIT", "TV"]
		subjects_like = ["PV", "DS", "PSS"]
		target_subjects = [13, 1, 2, 3, 4, 5, 6, 9, 10]
		for i in range(5):
			# RULE 1
			# want first hours
			if week[0 + i * 10] != 0:
				score += 149
			
			if week[8 + i * 10] != 0:
				score -= 50
			
			if week[9 + i * 10] != 0:
				score -= 100
			# RULE 3
			for j in range(9):
				if not self.same_classroom(self.subject_dict[week[j + i * 10]],
				                           self.subject_dict[week[j + 1 + i * 10]]):
					score -= 3
				if not self.same_floor(self.subject_dict[week[j + i * 10]], self.subject_dict[week[j + 1 + i * 10]]):
					score -= 34
			# RULE 4
			if week[4 + i * 10] == 0 or week[5 + i * 10] == 0 or week[6 + i * 10] == 0 or \
					week[7 + i * 10] == 0:
				score += 170
			else:
				score -= 10000
			
			# RULE 5
			if self.subject_dict[week[7 + i * 10]] != "X":
				score -= 80
			
			if self.subject_dict[week[8 + i * 10]] != "X":
				score -= 90
			
			if self.subject_dict[week[9 + i * 10]] != "X":
				score -= 10000
			
			# RULE 6
			k = 0
			while k < 9:
				if self.laboratory(self.subject_dict[week[k + i * 10]]):
					if self.same_subject_laboratory(self.subject_dict[week[k + i * 10]],
					                                self.subject_dict[week[k + 1 + i * 10]]):
						score += 300
						k += 1
					else:
						score -= 40
				k += 1
			
			# RULE 7
			if week[0 + i * 10] in target_subjects:
				score -= 23
			
			lunch_break = [5, 6, 7, 8]
			for j in lunch_break:
				if week[j + i * 10] == 0 and week[j + 1 + i * 10] in target_subjects:
					score -= 60
					break
			# RULE 8
			for j in range(8):
				
				if self.name(self.subject_dict[week[j + i * 10]]) == "M" and self.name(
						self.subject_dict[week[j + 1 + i * 10]]) == "AM" or self.name(
					self.subject_dict[week[j + i * 10]]) == "AM" and \
						self.name(self.subject_dict[week[j + 1 + i * 10]]) == "M":
					score -= 30
			# RULE 9
			if self.name(self.subject_dict[week[0 + i * 10]]) == "TV":
				score -= 70
			# RULE 10
			for j in range(10):
				# print(self.subject_dict[week[j + i * 10]].name) here it prints
				if self.name(self.subject_dict[week[j + i * 10]]) in subjects_hate:
					score -= 170
				elif self.name(self.subject_dict[week[j + i * 10]]) in subjects_like:
					score += 500
		return score
	
	def same_floor(self, subject1, subject2):
		"""
		Checks if two subjects are on the same floor.

		:param subject1: First subject.
		:param subject2: Second subject.
		:return: True if the subjects are on the same floor, False otherwise.
		"""
		
		if subject1 != "X" and subject2 != "X":
			if not isinstance(subject1, Subject) or not isinstance(subject2, Subject):
				raise TypeError("Subject has to be Subject class")
			return subject1.floor == subject2.floor
		return False
	
	def same_subject(self, subject1, subject2):
		"""
		Checks if two subjects have the same name.

		:param subject1: First subject.
		:param subject2: Second subject.
		:return: True if the subjects have the same name, False otherwise.
		"""
		if subject1 != "X" and subject2 != "X":
			if not isinstance(subject1, Subject) or not isinstance(subject2, Subject):
				raise TypeError("Subject has to be Subject class")
			return subject1.name == subject2.name
		return False
	
	def same_subject_laboratory(self, subject1, subject2):
		"""
		Checks if two subjects have the same name and are laboratory classes.

		:param subject1: First subject.
		:param subject2: Second subject.
		:return: True if the subjects have the same name and are laboratory classes, False otherwise.
		"""
		if subject1 != "X" and subject2 != "X":
			if not isinstance(subject1, Subject) or not isinstance(subject2, Subject):
				raise TypeError("Subject has to be Subject class")
			return subject1.name == subject2.name and subject1.laboratory and subject2.laboratory
		return False
	
	def same_classroom(self, subject1, subject2):
		"""
		Checks if two subjects are in the same classroom.
		
		:param subject1: First subject.
		:param subject2: Second subject.
		:return: True if the subjects are in the same classroom, False otherwise.
		"""
		if subject1 != "X" and subject2 != "X":
			if not isinstance(subject1, Subject) or not isinstance(subject2, Subject):
				raise TypeError("Subject has to be Subject class")
			return subject1.classroom == subject2.classroom
		return False
	
	def laboratory(self, subject):
		"""
		Checks if a subject is a laboratory class.
		
		:param subject: The subject to check.
		:return: True if the subject is a laboratory class, False otherwise.
		"""
		if subject != "X":
			if not isinstance(subject, Subject):
				raise TypeError("Subject has to be Subject class")
			return subject.laboratory
		return False
	
	def name(self, subject):
		"""
		Returns the name of a subject.
		
		:param subject: The subject.
		:return: The name of the subject.
		"""
		if subject != "X":
			if not isinstance(subject, Subject):
				raise TypeError("Subject has to be Subject class")
			return subject.name
		return "X"
