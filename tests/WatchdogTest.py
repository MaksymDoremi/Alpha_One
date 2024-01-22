import multiprocessing
import unittest
import sys
import os
sys.path.append('../Alpha_One')
from src.package import Watchdog


class WatchDogTest(unittest.TestCase):
	def test_watchdog_run_error(self):
		watchdog = Watchdog()
		process = multiprocessing.Process()
		
		with self.assertRaises(TypeError):
			watchdog.watchdog_timer("a",[process])
		
		with self.assertRaises(ValueError):
			watchdog.watchdog_timer(-3,[process])
		
		with self.assertRaises(TypeError):
			watchdog.watchdog_timer(4,"not list")
		
		with self.assertRaises(TypeError):
			watchdog.watchdog_timer(4,[1,2,3])