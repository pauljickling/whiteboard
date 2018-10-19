from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import Context, Template
from django.template.loader import get_template
from django.utils import timezone
from .forms import AnswerForm
from .models import Problem, Answer
import random

# Takes url path and converts it back to a Problem.category string
def de_urlify(path):
	str1 = path.strip('/')
	str2 = str1.replace('-', ' ')
	str3 = str2.title()
	return str3

# Defines categories for Navbar
categories = set(["All",])
for problem in problems:
	categories.add(problem.category)
sorted_categories = sorted(categories)

def problem(request, problem_id):
	try:
		current_problem = Problem.objects.get(id=problem_id)
		context = {
			'problem': current_problem,
			'form': AnswerForm,
			'category_nav': sorted_categories,
		}
	except Problem.DoesNotExist:
		raise Http404('Oh no, that problem does not exist!')
	return render(request, 'problems/index.html', context)

def index(request):
	problems = Problem.objects.all()
	problem_id_list = []
	for problem in problems:
		problem_id_list.append(problem.id)
	random_id = random.choice(problem_id_list)
	url = 'problem/' + str(random_id)
	return redirect(url)

def arrays_and_strings(request):
	array_problems = Problem.objects.filter(category='Arrays and Strings')
	array_ids = []
	for problem in array_problems:
		array_ids.append(problem.id)
	random_array = random.choice(array_ids)
	url = 'arrays-and-strings/problem/' + str(random_array)
	return redirect(url)

def linked_lists(request):
	list_problems = Problem.objects.filter(category='Linked Lists')
	list_ids = []
	for problem in list_problems:
		list_ids.append(problem.id)
	random_list = random.choice(list_ids)
	url = 'linked-lists/problem/' + str(random_list)
	return redirect(url)

def object_oriented_design(request):
	oop_problems = Problem.objects.filter(category='Object Oriented Design')
	oop_ids = []
	for problem in oop_problems:
		oop_ids.append(problem.id)
	random_oop = random.choice(oop_ids)
	url = 'object-oriented-design/problem/' + str(random_oop)
	return redirect(url)

def recursion(request):
	recursion_problems = Problem.objects.filter(category='Recursion and Dynamic Programming')
	recursion_ids = []
	for problem in recursion_problems:
		recursion_ids.append(problem.id)
	random_recursion = random.choice(recursion_ids)
	url = 'recursion-and-dynamic-programming/problem/' + str(random_recursion)
	return redirect(url)

def sorting(request):
	sorting_problems = Problem.objects.filter(category='Sorting and Searching')
	sorting_ids = []
	for problem in sorting_problems:
		sorting_ids.append(problem.id)
	random_sorting = random.choice(sorting_ids)
	url = 'sorting-and-searching/problem/' + str(random_sorting)
	return redirect(url)

def stacks(request):
	stack_problems = Problem.objects.filter(category='Stacks and Queues')
	stack_ids = []
	for problem in stack_problems:
		stack_ids.append(problem.id)
	random_stack = random.choice(stack_ids)
	url = 'stacks-and-queues/problem/' + str(random_stack)
	return redirect(url)

def scaling(request):
	scaling_problems = Problem.objects.filter(category='System Design and Scalability')
	scaling_ids = []
	for problem in scaling_problems:
		scaling_ids.append(problem.id)
	random_scaling = random.choice(scaling_ids)
	url = 'system-desing-and-scalability/problem/' + str(random_scaling)
	return redirect(url)

def testing(request):
	testing_problems = Problem.objects.filter(category='Testing and Debugging')
	testing_ids = []
	for problem in testing_problems:
		testing_ids.append(problem.id)
	random_testing = random.choice(testing_ids)
	url = 'testing-and-debugging/problem/' + str(random_testing)
	return redirect(url)

def graphs(request):
	graph_problems = Problem.objects.filter(category='Trees and Graphs')
	graph_ids = []
	for problem in graph_problems:
		graph_ids.append(problem.id)
	random_graph = random.choice(graph_ids)
	url = 'trees-and-graphs/problem/' + str(random_graph)
	return redirect(url)


def answers(request):
	answers = Answer.objects.all()
	return render(request, 'problems/answers.html', {'answers': answers})