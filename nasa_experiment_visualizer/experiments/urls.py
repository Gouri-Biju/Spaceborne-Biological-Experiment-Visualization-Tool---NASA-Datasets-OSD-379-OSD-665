from django.contrib import admin
from django.urls import path
from . import views
from .views import experiment_create, evaluation, result, results, graphs, form


urlpatterns = [
    path('', views.experiment_create, name='experiment_create'),
    path('evaluation/', evaluation, name='evaluation'),
    path('result/', result, name='result'),
    path('results/', results, name='results'),
    path('graphs/',graphs,name='graphs'),
    path('form/',form,name='form'),
]