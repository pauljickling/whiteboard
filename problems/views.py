from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import Context, Template
from django.template.loader import get_template
from django.forms import ModelForm, Textarea, Select
from django.utils import timezone
from .models import Problem, Answer
from .random_problem import select_problem, problem_list
import random

problems = Problem.objects.all()
problem_id_list = []
for problem in problems:
	problem_id_list.append(problem.id)
print(problem_id_list)
random_id = random.choice(problem_id_list)
print("Random ID: ", random_id)

def instance(request, problem_id):
	try:
		p = Problem.objects.get(id=problem_id)
	except Problem.DoesNotExist:
		raise Http404('Oh no, that problem does not exist!')
	return render(request, 'problems/instance.html', {'problem': p})

def index(request):

	# Takes url path and converts it back to a Problem.category string
	def de_urlify(path):
		str1 = path.lstrip('/')
		str2 = str1.replace('-', ' ')
		str3 = str2.title()
		return str3
	
	current_path = de_urlify(request.path)

	# Selects current problem from problem_list (See random_problem.py)
	current_problem = problem_list[current_path]
	PROBLEM_CHOICE = (current_problem,)

	# Defines problems for categories
	problems = Problem.objects.all()
	arrays = Problem.objects.filter(category='Arrays and Strings')
	linked_lists = Problem.objects.filter(category='Linked Lists')
	oop = Problem.objects.filter(category='Object Oriented Design')
	recursion = Problem.objects.filter(category='Recursion and Dynamic Programming')
	sorting = Problem.objects.filter(category='Sorting and Searching')
	stacks = Problem.objects.filter(category='Stacks and Queues')
	scaling = Problem.objects.filter(category='System Design and Scalability')
	testing = Problem.objects.filter(category='Testing and Debugging')
	graphs = Problem.objects.filter(category='Trees and Graphs')
	print(len(arrays))
	#creates answer form
	class AnswerForm(ModelForm):
		class Meta:
			model = Answer
			fields = ['answer', 'language', 'problem']
			widgets = {
				'answer': Textarea(attrs={'cols': 80, 'rows': 20}),
			}	

	# Defines categories for Navbar
	categories = set(["All",])
	for problem in problems:
		categories.add(problem.category)
	sorted_categories = sorted(categories)

	# Looks up answers for current problem
	answers = Answer.objects.all()
	current_answers = []
	for answer in answers:
		if answer.problem == current_problem:
			current_answers.append(answer)

	# Context for template engine
	context = {
		'random_problem': current_problem, 
		'form': AnswerForm,
		'current_answers': current_answers,
		'problem_category': sorted_categories}

	print(context['random_problem'])

	# Handles POST request
	if request.method == "POST":
		answer = AnswerForm(request.POST)
		
		if answer.is_valid():
			instance = answer.save(commit=False)
			instance.correct = False
			instance.answer_date = timezone.now()
			instance.save()
			return render(request, 'problems/index.html', context)
	
	# Handles GET request
	else:
		return render(request, 'problems/index.html', context)

def answers(request):
	answers = Answer.objects.all()
	context = {
		'answers': answers,
	}
	return render(request, 'problems/answers.html', context)