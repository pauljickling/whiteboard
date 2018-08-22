from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import Context, Template
from django.template.loader import get_template
from django.forms import ModelForm, Textarea
from django.utils import timezone
from .models import Problem, Answer
import random

def index(request):

	class AnswerForm(ModelForm):
		class Meta:
			model = Answer
			fields = ['answer', 'language']
			widgets = {
				'answer': Textarea(attrs={'cols': 80, 'rows': 20}),
			}	
	
	# Takes url path and converts it back to a Problem.category string
	def de_urlify(path):
		str1 = path.lstrip('/')
		str2 = str1.replace('-', ' ')
		str3 = str2.title()
		return str3

	# Select random problem based on current category
	def current_category(problem):
		random_problem = random.choice(problem)
		current_path = request.path
		user_selection = de_urlify(current_path)

		if user_selection == '':
			user_selection = 'All'

		if user_selection == 'All':
			return random_problem

		while random_problem.category != user_selection:
			random_problem = random.choice(problem)
			if random_problem.category == user_selection:
				break

		return random_problem


	problems = Problem.objects.all()
	random_problem = current_category(problems)

	# Uncomment line below for testing
	#random_problem = problems[0] 

	categories = set(["All",])
	for i in problems:
		categories.add(i.category)
	sorted_categories = sorted(categories)

	answers = Answer.objects.all()
	current_answers = []
	for i in answers:
		if i.problem == random_problem:
			current_answers.append(i)

	context = {
		'random_problem': random_problem, 
		'form': AnswerForm,
		'current_answers': current_answers,
		'problem_category': sorted_categories}

	if request.method == "POST":
		answer = AnswerForm(request.POST)
		
		if answer.is_valid():
			instance = answer.save(commit=False)
			instance.correct = False
			instance.answer_date = timezone.now()
			instance.problem = random_problem
			instance.save()
			return render(request, 'problems/index.html', context)
	else:
		return render(request, 'problems/index.html', context)