from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import Context, Template
from django.template.loader import get_template
from django.utils import timezone
from .forms import AnswerForm
from .models import Problem, Answer
import random

problems = Problem.objects.all()
problem_id_list = []
for problem in problems:
	problem_id_list.append(problem.id)
random_id = random.choice(problem_id_list)

# Defines categories for Navbar
categories = set(["All",])
for problem in problems:
	categories.add(problem.category)
sorted_categories = sorted(categories)
print(sorted_categories)

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
	route = 'problem/' + str(random_id)
	print(route)
	return redirect(route)

def category(request, category, problem_id):
	pass

def answers(request):
	answers = Answer.objects.all()
	return render(request, 'problems/answers.html', {'answers': answers})