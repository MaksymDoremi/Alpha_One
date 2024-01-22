import math
import multiprocessing

from src.package import Subject
# subject dictionary, decoding
subject_dictionary = {
	0: "X",
	1: Subject("PV", "Mgr. Alena Reichlová & Ing. Ondřej Mandík", "18b", 3, True),
	2: Subject("PV", "Mgr. Alena Reichlová", "24", 4, False),
	3: Subject("WA", "Mgr. Jan Pavlát", "17a", 3, True),
	4: Subject("WA", "Mgr. Jan Pavlát", "24", 4, False),
	5: Subject("DS", "Ing. Ivana Kantnerová", "18a", 3, True),
	6: Subject("DS", "Ing. Ivana Kantnerová", "24", 4, False),
	7: Subject("PIS", "Ing. Lucie Brčáková", "24", 4, False),
	8: Subject("PIS", "Ing. Lucie Brčáková", "19a", 3, True),
	9: Subject("PSS", "Ing. Lukáš Masopust", "24", 4, False),
	10: Subject("PSS", "Ing. Lukáš Masopust", "8a", 1, True),
	11: Subject("C", "MUDr. Kristina Studénková", "24", 4, False),
	12: Subject("A", "Ing. Tomáš Juchelka", "5a", 1, False),
	13: Subject("M", "Mgr. Eva Neugebauerová", "24", 4, False),
	14: Subject("TP", "Ing. Vít Nohejl", "24", 4, False),
	15: Subject("TV", "Mgr. Pavel Lopocha", "TV", 0, False),
	16: Subject("AM", "Ing. Filip Kallmünzer", "24", 4, False),
	17: Subject("CIT", "Mgr. Jakub Mazuch", "17b", 3, True),
}

# input schedule
schedule = [
	3, 3, 11, 12, 13, 0, 1, 1, 0, 0,
	13, 14, 5, 5, 12, 16, 0, 15, 0, 0,
	7, 11, 17, 17, 16, 13, 6, 0, 0, 0,
	4, 13, 7, 2, 12, 11, 9, 0, 0, 0,
	0, 8, 8, 12, 15, 10, 10, 0, 0, 0
]
# get cpu cores count and minus 1 (that is watchdog in main thread)
process_count = multiprocessing.cpu_count() - 1

# divide ration of generators to evaluators to be 1:3
evaluator_process_count = math.floor(process_count / 4 * 3)
generator_process_count = math.ceil(process_count / 4)

# timeout for the watchdog
timeout = 180
# every N seconds generator will update the shared list of the schedules
every_n_seconds = 2
