import multiprocessing
import time


class Watchdog:
	"""
	Watchdog class used to check for timeout and terminate processes if the timeout is exceeded.
	After exceeding the given timeout, it kills all the other processes in the provided pool.
	"""
	
	def __init__(self):
		"""
		Initializes a Watchdog instance.
		"""
		pass
	
	def watchdog_timer(self, timeout, pool):
		"""
		Watchdog method that serves as the main process. It is designed to be used because
		of the pool list to keep references to other generator and evaluator processes.

		:param timeout: The timeout in seconds.
		:param pool: A pool of processes to terminate if the timeout is exceeded.
		:return: None
		"""
		if not isinstance(timeout,(int, float)):
			raise TypeError("Timeout can't be zero")
		
		if timeout <= 0:
			raise ValueError("Timeout can't be <= 0")
		
		if not isinstance(pool, list):
			raise TypeError("Pool has to be list, []")
		
		if not all(isinstance(process, multiprocessing.Process) for process in pool):
			raise TypeError("Items in pool has to be processes")
		
		print("WATCHDOG")
		time.sleep(timeout)
		
		for process in pool:
			process.kill()
		print("GLOBAL SHUTDOWN")
