from django.shortcuts import render
from django.http import HttpResponse
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
	
	problems = Problem.objects.all()
	random_problem = random.choice(problems)

	# Uncomment line below for testing
	# random_problem = problems[0] 

	answers = Answer.objects.all()
	current_answers = []
	for i in answers:
		if i.problem == random_problem:
			current_answers.append(i)

	context = {
		'random_problem': random_problem, 
		'form': AnswerForm,
		'current_answers': current_answers}

	if request.method == "POST":
		answer = AnswerForm(request.POST)
		
		if answer.is_valid():
			instance = answer.save(commit=False)
			instance.correct = False
			instance.answer_date = timezone.now()
			instance.problem = random_problem
			instance.save()
			return render(request, 'questions/index.html', context)
	else:
		return render(request, 'questions/index.html', context)