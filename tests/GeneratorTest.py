import multiprocessing
import unittest
import sys
import os
sys.path.append('../Alpha_One')
from src.package import Generator

class GeneratorTest(unittest.TestCase):
	def test_generator_run_error(self):
		generator = Generator()

		schedule = [1,2,3,4,5]
		final_schedules = multiprocessing.Manager().list()
		every_n_seconds = 2
		generated_overall = multiprocessing.Value("i",0)
		
		with self.assertRaises(TypeError):
			generator.generate_shuffle("a", final_schedules, every_n_seconds, generated_overall)
		
		with self.assertRaises(TypeError):
			generator.generate_shuffle(["a",1,2,3], final_schedules, every_n_seconds, generated_overall)
			
		with self.assertRaises(TypeError):
			generator.generate_shuffle(schedule, [], every_n_seconds, generated_overall)
		
		with self.assertRaises(TypeError):
			generator.generate_shuffle(schedule, final_schedules, "a", generated_overall)
		
		with self.assertRaises(ValueError):
			generator.generate_shuffle(schedule, final_schedules, -4, generated_overall)
		
		with self.assertRaises(TypeError):
			generator.generate_shuffle(schedule, final_schedules, every_n_seconds, "a")
	