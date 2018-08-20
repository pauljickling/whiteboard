from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
path('', views.index, name='problems'),
path('all', views.index, name='all'),
path('arrays-and-strings', views.index, name='arrays-and-strings'),
path('javascript-problems', views.index, name='javascript-problems'),
path('linked-lists', views.index, name='linked-lists'),
path('math-and-logic-puzzles', views.index, name='math-and-logic-puzzles'),
path('object-oriented-design', views.index, name='object-oriented-design'),
path('recursion-and-dynamic-programming', views.index, name='recursion-and-dynamic-programming'),
path('sorting-and-searching', views.index, name='sorting-and-searching'),
path('stacks-and-queues', views.index, name='stacks-and-queues'),
path('system-design-and-scalability', views.index, name='system-design-and-scalability'),
path('testing-and-debugging', views.index, name='testing-and-debugging'),
path('trees-and-graphs', views.index, name='trees-and-graphs'),
]