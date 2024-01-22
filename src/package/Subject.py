class Subject:
	"""
	Subject class representing one school subject.
	Contains name, teacher who teaches, classroom, floor where it is taught, and whether it is a laboratory or theory class.
	"""
	
	def __init__(self, name: str, teacher: str, classroom: str, floor: int, laboratory: bool):
		"""
		Initializes a Subject object with specified attributes.

		:param name: The name of the school subject.
		:param teacher: The teacher who teaches the subject.
		:param classroom: The classroom where the subject is taught.
		:param floor: The floor on which the subject's classroom is located.
		:param laboratory: A boolean indicating whether the subject is a laboratory class (True) or a theory class (False).
		"""
		self._name = None
		self._teacher = None
		self._classroom = None
		self._floor = None
		self._laboratory = None
		
		self.name = name
		self.teacher = teacher
		self.classroom = classroom
		self.floor = floor
		self.laboratory = laboratory
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		if isinstance(value, str):
			self._name = value
		else:
			raise TypeError("Name of the subject has to be string!")
	
	@property
	def teacher(self):
		return self._teacher
	
	@teacher.setter
	def teacher(self, value):
		if isinstance(value, str):
			self._teacher = value
		else:
			raise TypeError("Teacher of the subject has to be string!")
	
	@property
	def classroom(self):
		return self._classroom
	
	@classroom.setter
	def classroom(self, value):
		if isinstance(value, str):
			self._classroom = value
		else:
			raise TypeError("Classroom of the subject has to be string!")
	
	@property
	def floor(self):
		return self._floor
	
	@floor.setter
	def floor(self, value):
		if isinstance(value, int):
			self._floor = value
		else:
			raise TypeError("Floor of the subject has to be int!")
	
	@property
	def laboratory(self):
		return self._laboratory
	
	@laboratory.setter
	def laboratory(self, value):
		if isinstance(value, bool):
			self._laboratory = value
		else:
			raise TypeError("Floor of the subject has to be bool!")
	
	def __str__(self):
		"""
		Returns a string representation of the Subject.

		:return: A string containing the name, teacher, classroom, floor, and whether it is a laboratory or theory class.
		"""
		return f"{self.name} {self.teacher} {self.classroom} {self.floor} {'laboratory' if self.laboratory else 'theory'}"
