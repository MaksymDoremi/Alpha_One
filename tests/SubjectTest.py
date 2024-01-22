import unittest
import sys
import os
sys.path.append('../Alpha_One')
from src.package import Subject


class SubjectTest(unittest.TestCase):
	def test_subject_create(self):
		subject = Subject("PV", "Mgr. Alena Reichlová", "24", 4, False)
		
		self.assertEqual(subject.name, "PV")
		self.assertEqual(subject.teacher, "Mgr. Alena Reichlová")
		self.assertEqual(subject.classroom, "24")
		self.assertEqual(subject.floor, 4)
		self.assertFalse(subject.laboratory)
		
		with self.assertRaises(TypeError):
			subject_error = Subject(1, 2, 3, 4, 5)
		
		self.assertEqual(subject.__str__(), "PV Mgr. Alena Reichlová 24 4 theory")
	
	def test_subject_change(self):
		subject = Subject("PV", "Mgr. Alena Reichlová", "24", 4, False)
		
		with self.assertRaises(TypeError):
			subject.teacher = 4
		
		with self.assertRaises(TypeError):
			subject.classroom = 4
		
		with self.assertRaises(TypeError):
			subject.floor = "4"
		
		with self.assertRaises(TypeError):
			subject.laboratory = 4
		
		with self.assertRaises(TypeError):
			subject.laboratory = "aaa"
	
	def test_subject_print(self):
		subject = Subject("PV", "Mgr. Alena Reichlová", "24", 4, False)
		
		self.assertEqual(subject.__str__(), "PV Mgr. Alena Reichlová 24 4 theory")
		subject.laboratory = True
		self.assertEqual(subject.__str__(), "PV Mgr. Alena Reichlová 24 4 laboratory")
