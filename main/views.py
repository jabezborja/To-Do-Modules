# Imports
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from .models import Task, TaskNote
from .forms import NewTaskForm, NoteForm
from django.contrib import messages

# Home View Render
def home(request):
	# Form for New Task
	form = NewTaskForm(request.POST or None)

	# Filter tasks to see in the home
	task = Task.objects.filter(archived=False).order_by('week_num')

	# Context to pass
	context = {'task': task}

	# To see if the request method has post.
	if request.method != 'POST':
		return render(request, 'home.html', context)

	# Check if the form is not valid them redirect to Home.html
	if not form.is_valid():
		return render(request, 'home.html', context)

 	# Get all the form in the home.html
	title = form.cleaned_data['title']
	desc = form.cleaned_data['desc']
	summary = form.cleaned_data['summary']
	subject = form.cleaned_data['subject']
	week_num = form.cleaned_data['week_num']

	# Ready to save
	register = Task(
		title=title,
		desc=desc,
		summary=summary,
		subject=subject,
		week_num=week_num
	)

	register.save()
	messages.success(request, "Task successfully added")
	return render(request, 'home.html', context)

# Tasks that are done render
def tasks_done(request):
	task = Task.objects.filter(archived=True).order_by('-week_num')

	context = {'task': task}
	return render(request, 'done_tasks.html', context)

# See clicked task render
def viewtask(request, id):
	task = Task.objects.get(pk=id)
	notes = TaskNote.objects.filter(task__id=id)
	form = NoteForm(request.POST or None)

	if request.method == "POST":
		if form.is_valid():
			note = form.save(commit=False)
			note.task = task
			note.save()
			messages.success(request, "Noted!")
			return HttpResponseRedirect(f'/task/{id}')

	return render(request, 'task.html', {'task': task, 'notes': notes, 'form': form})

# Done task button execute
def done_task(request, task_id):
	task = Task.objects.get(id=task_id)
	post_archive = task.archived

	post_archive = True
	task.archived = post_archive
	task.save()

	messages.success(request, "Task archived!")
	return HttpResponseRedirect(reverse('home'))

# Return task button execute
def return_task(request, task_id):
	task = Task.objects.get(id=task_id)
	post_archive = task.archived

	post_archive = False
	task.archived = post_archive
	task.save()

	messages.success(request, "Task returned!")
	return HttpResponseRedirect(reverse('tasks_done'))

# Delete task button execute
def delete_task(request, task_id):
	task = Task.objects.get(id=task_id)

	task.delete()
	messages.warning(request, "Task deleted!")
	return HttpResponseRedirect(reverse('tasks_done'))
