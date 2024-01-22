import sys
import os
sys.path.append('../Alpha_One')

from config import *
from package import *
import multiprocessing

def main():
	"""
	Main function orchestrating the generation and evaluation of school schedules.
	"""
	
	# Manager for shared objects in multiprocessing
	manager = multiprocessing.Manager()
	
	# Initialize Generator, Watchdog, and Evaluator
	generator = Generator()
	watchdog = Watchdog()
	evaluator = Evaluator()
	
	# Shared lists and values for communication between processes
	final_week_schedules = manager.list()
	best_schedules = manager.list()
	better_than_input_schedules = manager.list()
	generated_overall = multiprocessing.Value("i", 0)
	# Process pool for parallel execution
	pool = []
	
	# Evaluate the input schedule to compare against generated schedules
	input_schedule_score = evaluator.evaluate(schedule)
	
	# Start generator processes
	for _ in range(generator_process_count):
		process = multiprocessing.Process(target=generator.generate_shuffle,
		                                  args=(schedule, final_week_schedules, every_n_seconds, generated_overall,))
		pool.append(process)
	
	# Start evaluator processes
	for _ in range(evaluator_process_count):
		evaluator_proc = multiprocessing.Process(target=evaluator.evaluate_process, args=(
			final_week_schedules, best_schedules, input_schedule_score, better_than_input_schedules,))
		pool.append(evaluator_proc)
	
	# Start all processes in the pool
	for process in pool:
		process.start()
	
	# Start the watchdog timer to manage the overall execution time
	watchdog.watchdog_timer(timeout, pool)
	
	# Calculate and print evaluation results
	evaluated = generated_overall.value - len(final_week_schedules)
	print(f"Generated overall: {generated_overall.value}")
	print(f"Evaluated overall: {evaluated}")
	print(f"Best schedules, score > 0: {len(best_schedules)}")
	print(f"Schedules better than input schedule: {len(better_than_input_schedules)}")
	print("")
	print("================================================================================")
	print("================================================================================")
	
	# Sort and print the best schedules
	sorted_schedules = sorted(best_schedules, key=lambda week: week[50], reverse=True)
	for week in sorted_schedules:
		result = ""
		for i in range(5):
			for j in range(10):
				if subject_dictionary[week[j + i * 10]] != "X":
					result += f"{subject_dictionary[week[j + i * 10]].name}, "
				else:
					result += "X, "
			result += "\n"
		print(result)
		print(f"Score {week[50]}")
		print("================================================================================")
		print("================================================================================")


if __name__ == '__main__':
	main()
