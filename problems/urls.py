from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
path('', views.index, name='problems'),
path('all', views.index, name='problems'),
path('arrays-and-strings', views.index, name='problems'),
path('javascript-problems', views.index, name='problems'),
path('linked-lists', views.index, name='problems'),
path('math-and-logic-puzzles', views.index, name='problems'),
path('object-oriented-design', views.index, name='problems'),
path('recursion-and-dynamic-programming', views.index, name='problems'),
path('sorting-and-searching', views.index, name='problems'),
path('stacks-and-queues', views.index, name='problems'),
path('system-design-and-scalability', views.index, name='problems'),
path('testing-and-debugging', views.index, name='problems'),
path('trees-and-graphs', views.index, name='problems'),
]