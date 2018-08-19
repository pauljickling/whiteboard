from django.db import models
from django.utils import timezone

ALL = "All"
NON_CODING = "Non_Coding"
ARRAYS_AND_STRINGS = "Arrays and Strings"
LINKED_LISTS = "Linked Lists"
STACKS_AND_QUEUES = "Stacks and Queues"
TREES_AND_GRAPHS = "Trees and Graphs"
BIT_MANIPULATION = "Bit Manipulation"
MATH_AND_LOGIC_PUZZLES = "Math and Logic Puzzles"
OBJECT_ORIENTED_DESIGN = "Object Oriented Design"
RECURSION_AND_DYNAMIC_PROGRAMMING = "Recursion and Dynamic Programming"
SYSTEM_DESIGN_AND_SCALABILITY = "System Design and Scalability"
SORTING_AND_SEARCHING = "Sorting and Searching"
TESTING = "Testing"
JAVASCRIPT = "Javascript"

CATEGORY_CHOICES = (
	(ALL, "All"),
	(NON_CODING, "Non-Coding"),
	(ARRAYS_AND_STRINGS, 'Arrays and Strings'),
	(LINKED_LISTS, 'Linked Lists'),
	(STACKS_AND_QUEUES, 'Stacks and Queues'),
	(TREES_AND_GRAPHS, 'Trees and Graphs'),
	(BIT_MANIPULATION, 'Bit Manipulation'),
	(MATH_AND_LOGIC_PUZZLES, 'Math and Logic Puzzles'),
	(OBJECT_ORIENTED_DESIGN, 'Object Oriented Design'),
	(RECURSION_AND_DYNAMIC_PROGRAMMING, 'Recursion and Dynamic Programming'),
	(SYSTEM_DESIGN_AND_SCALABILITY, 'System Design and Scalability'),
	(SORTING_AND_SEARCHING, 'Sorting and Searching'),
	(TESTING, 'Testing'),
	(JAVASCRIPT, 'Javascript')
)

class Problem(models.Model):
	problem = models.TextField()
	starred = models.BooleanField(default=False)
	category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=ALL)

	def __str__(self):
		return self.problem

PSEUDOCODE = "Psuedocode"
CPLUSPLUS = "C++"
GO = "Go"
JAVA = "Java"
JAVASCRIPT = "Javascript"
PYTHON = "Python"
RUBY = "Ruby"
RUST = "Rust"
WRITING = "Writing"

LANGUAGE_CHOICES = (
	(PSEUDOCODE, 'Psuedocode and/or Writing'),
	(CPLUSPLUS, 'C++'),
	(GO, 'Go'),
	(JAVA, 'Java'),
	(JAVASCRIPT, 'Javascript'),
	(PYTHON, 'Python'),
	(RUBY, 'Ruby'),
	(RUST, 'Rust'),
	(WRITING, 'Writing')
)

class Answer(models.Model):
	answer = models.TextField()
	language = models.CharField(max_length=30, choices = LANGUAGE_CHOICES, default=JAVASCRIPT)
	correct = models.BooleanField(default=False)
	answer_date = models.DateTimeField(null=True)
	problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.answer
		self.problem

