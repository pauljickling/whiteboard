from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from django.template.loader import get_template
from .models import Problem
import random

def index(request):
	problems = Problem.objects.all()
	random_problem = random.choice(problems)
	title = "Project Title"
	context = {'random_problem': random_problem,}

	return render(request, 'questions/index.html', context)