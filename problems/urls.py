from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('problem/<int:problem_id>', views.problem, name='problem'),
path('arrays-and-strings', views.arrays_and_strings, name='arrays-and-strings'),
path('arrays-and-strings/problem/<int:problem_id>', views.problem, name='array-problem'),
path('linked-lists', views.linked_lists, name='linked-lists'),
path('linked-lists/problem/<int:problem_id>', views.problem, name='linked-list-problem'),
path('object-oriented-design', views.object_oriented_design, name='object-oriented-design'),
path('object-oriented-design/problem.<int:problem_id>', views.index, name='object-oriented-design-problem'),
path('recursion-and-dynamic-programming', views.recursion, name='recursion-and-dynamic-programming'),
path('recursion-and-dynamic-programming/problem/<int:problem_id>', views.index, name='recursion-and-dynamic-programming-problem'),
path('sorting-and-searching', views.sorting, name='sorting-and-searching'),
path('sorting-and-searching/problem/<int:problem_id>', views.index, name='sorting-and-searching-problem'),
path('stacks-and-queues', views.stacks, name='stacks-and-queues'),
path('stacks-and-queues/problem/<int:problem_id>', views.index, name='stacks-and-queues-problem'),
path('system-design-and-scalability', views.scaling, name='system-design-and-scalability'),
path('system-design-and-scalability/problem/<int:problem_id>', views.index, name='system-design-and-scalability/problem'),
path('testing-and-debugging', views.testing, name='testing-and-debugging'),
path('testing-and-debugging/problem/<int:problem_id>', views.index, name='testing-and-debugging-problem'),
path('trees-and-graphs', views.graphs, name='trees-and-graphs'),
path('trees-and-graphs/problem/<int:problem_id>', views.index, name='trees-and-graphs/problem'),
path('answers', views.answers, name='answers'),
]