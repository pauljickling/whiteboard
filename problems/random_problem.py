from .models import Problem, Answer
import random

def select_problem(category):
	current_category = category
	problems = Problem.objects.all()
	any_problem = random.choice(problems)

	if current_category == '':
		current_category = 'Any'

	if current_category == 'Any':
		return any_problem
	else:
		category_problems = []
		for problem in problems:
			if problem.category == current_category:
				category_problems.append(problem)

		# Saftety measure
		while category_problems == []:
			return "Sorry, something went wrong and we weren't able to retrieve a random problem. Please file an issue at https://github.com/pauljickling/whiteboard/issues"

		category_problem = random.choice(category_problems)
		return category_problem

any_problem = select_problem('Any')
arrays_strings_problem = select_problem('Arrays and Strings')
linked_list_problem = select_problem('Linked Lists')
stacks_queues_problem = select_problem('Stacks and Queues')
graph_problem = select_problem('Trees and Graphs')
oop_problem = select_problem('Object Oriented Design')
recursion_dynamic_problem = select_problem('Recursion and Dynamic Programming')
scale_problem = select_problem('System Design and Scalability')
sort_search_problem = select_problem('Sorting and Searching')
testing_problem = select_problem('Testing and Debugging')

problem_list = {
	'': any_problem, 
	'All': any_problem,
	'Strings And Arrays': arrays_strings_problem,
	'Linked Lists':	linked_list_problem,
	'Stacks And Queues': stacks_queues_problem,
	'Trees And Graphs':	graph_problem,
	'Object Oriented Design': oop_problem,
	'Recursion And Dynamic Programming': recursion_dynamic_problem,
	'System Design And Scalability': scale_problem,
	'Sorting And Searching': sort_search_problem,
	'Testing And Debugging': testing_problem
	}