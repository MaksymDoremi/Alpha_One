import multiprocessing.managers
import random
import time


class Generator:
	"""
	Generator class used to generate as many different variations of the school schedule as possible.
	"""
	
	def __init__(self):
		"""
		Initializes a Generator instance.
		"""
		pass
	
	def generate_shuffle(self, schedule, final_schedules, every_n_seconds, generated_overall):
		"""
		Generates different schedules using random.shuffle() and extends a shared list with the results.

		:param schedule: The input schedule.
		:param final_schedules: A manager.list() that stores all different schedules.
		:param every_n_seconds: The time interval in seconds at which the generator extends the shared list for the schedules.
		:param generated_overall: A shared variable indicating the overall number of schedules generated.
		:return: None
		"""
		if not isinstance(schedule, list):
			raise TypeError("Schedule has to be list, []")
		
		if not all(isinstance(subject, int) for subject in schedule):
			raise TypeError("Subject has to be represented as int")
		
		if not isinstance(final_schedules, multiprocessing.managers.ListProxy):
			raise TypeError("Final schedules has to be listproxy")
		
		if not isinstance(every_n_seconds, int):
			raise TypeError("Every n seconds has to be int")
		
		if every_n_seconds <= 0:
			raise ValueError("Every n seconds has to be > 0")
		
		if not isinstance(generated_overall, multiprocessing.sharedctypes.Synchronized):
			raise TypeError("generated overall has to be multiprocessing value")
		
		start = time.time()
		weeks = set()
		while True:
			random.shuffle(schedule)
			weeks.add(tuple(schedule))
			
			if time.time() >= start + every_n_seconds:
				final_schedules.extend(list(map(list, weeks)))
				generated_overall.value += len(weeks)
				weeks.clear()
				start = time.time()
