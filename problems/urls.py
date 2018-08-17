from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
path('', views.index, name='problems'),
#path('/<slug:slug>', views.problem_category, name='problem_category'),
]