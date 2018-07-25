from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from django.template.loader import get_template
from django.forms import ModelForm
from .models import Problem, Answer
import random

def index(request):

	class AnswerForm(ModelForm):
		class Meta:
			model = Answer
			fields = ['answer', 'language']

	problems = Problem.objects.all()
	random_problem = random.choice(problems)
	context = {'random_problem': random_problem, 'form': AnswerForm,}

	return render(request, 'questions/index.html', context)