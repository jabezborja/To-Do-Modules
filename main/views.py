# Imports
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from .models import Task, TaskNote
from .forms import NewTaskForm, NoteForm, DescForm
from django.contrib import messages

# Home View Render
def home(request):
	# Filter tasks to see in the home
	task = Task.objects.filter(archived=False).order_by('week_num')
	task_count = task.count()

	# Context to pass
	context = {'task': task, 'task_count': task_count}

	return render(request, 'home.html', context)

# Tasks that are done render
def tasks_done(request):
	task = Task.objects.filter(archived=True).order_by('-week_num')

	context = {'task': task}
	return render(request, 'done_tasks.html', context)

# Sched
def sched(request):
	return render(request, 'sched.html', {})

# Task View
def taskview(request):
	return HttpResponseRedirect(reverse('home'))