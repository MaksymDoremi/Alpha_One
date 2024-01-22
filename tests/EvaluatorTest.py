import multiprocessing
import unittest
import sys
import os
sys.path.append('../Alpha_One')

from src.package import Evaluator
from src.package import Subject


class EvaluatorTest(unittest.TestCase):
	def test_evaluator_run_error(self):
		evaluator = Evaluator()
		
		final_schedules = multiprocessing.Manager().list()
		best_schedules = multiprocessing.Manager().list()
		input_schedule_score = 0
		better_than_input_schedules = multiprocessing.Manager().list()
		
		with self.assertRaises(TypeError):
			evaluator.evaluate_process([], best_schedules, input_schedule_score, better_than_input_schedules)
		
		with self.assertRaises(TypeError):
			evaluator.evaluate_process(final_schedules, [], input_schedule_score, better_than_input_schedules)
		
		with self.assertRaises(TypeError):
			evaluator.evaluate_process(final_schedules, best_schedules, "aaa", better_than_input_schedules)
		
		with self.assertRaises(TypeError):
			evaluator.evaluate_process(final_schedules, best_schedules, input_schedule_score, [])
	
	def test_evaluator_evaluate_error(self):
		evaluator = Evaluator()
		
		with self.assertRaises(TypeError):
			evaluator.evaluate("aa")
		
		with self.assertRaises(ValueError):
			evaluator.evaluate([1, 2, 3, "a"])
	
	def test_evaluator_methods(self):
		evaluator = Evaluator()
		subject1 = Subject("WA", "Mgr. Jan Pavlát", "24", 4, False)
		subject2 = Subject("PV", "Mgr. Alena Reichlová", "24", 4, False)
		
		subjectLab1 = Subject("WA", "Mgr. Jan Pavlát", "17a", 3, True)
		subjectLab2 = Subject("WA", "Mgr. Jan Pavlát", "17a", 3, True)
		subjectLab3 = Subject("PV", "Mgr. Alena Reichlová & Ing. Ondřej Mandík", "18b", 3, True)
		
		self.assertEqual(evaluator.same_floor(subject1, subject2), True)
		self.assertEqual(evaluator.same_floor(subject1, subjectLab1), False)
		self.assertEqual(evaluator.same_floor(subject1, "X"), False)
		
		self.assertEqual(evaluator.same_classroom(subject1, subject2), True)
		self.assertEqual(evaluator.same_classroom(subject1, subjectLab1), False)
		self.assertEqual(evaluator.same_classroom(subject1, "X"), False)
		
		self.assertEqual(evaluator.same_subject(subject1, subject1), True)
		self.assertEqual(evaluator.same_subject(subject1, subject2), False)
		self.assertEqual(evaluator.same_subject(subject1, "X"), False)
		
		self.assertEqual(evaluator.same_subject_laboratory(subjectLab1, subjectLab2), True)
		self.assertEqual(evaluator.same_subject_laboratory(subjectLab1, subjectLab3), False)
		self.assertEqual(evaluator.same_subject_laboratory(subjectLab1, "X"), False)
		
		self.assertEqual(evaluator.name(subject1), "WA")
		self.assertEqual(evaluator.name("X"), "X")
		self.assertEqual(evaluator.laboratory(subject1), False)
		self.assertEqual(evaluator.laboratory("X"), False)
		self.assertEqual(evaluator.laboratory(subjectLab1), True)
		
		with self.assertRaises(TypeError):
			evaluator.same_subject(1, 2)
		
		with self.assertRaises(TypeError):
			evaluator.same_floor(1, 2)
		
		with self.assertRaises(TypeError):
			evaluator.same_classroom(1, 2)
		
		with self.assertRaises(TypeError):
			evaluator.same_subject_laboratory(1, 2)
		
		with self.assertRaises(TypeError):
			evaluator.name(1)
		
		with self.assertRaises(TypeError):
			evaluator.laboratory(1)
