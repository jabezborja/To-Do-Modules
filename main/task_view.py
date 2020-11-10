# Imports
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from .models import Task, TaskNote
from .forms import NewTaskForm, NoteForm, DescForm
from django.contrib import messages

# See clicked task render
def viewtask(request, id):
	task = Task.objects.get(pk=id)
	notes = TaskNote.objects.filter(task__id=id)
	form = NoteForm()

	return render(request, 'task.html', {'task': task, 'notes': notes, 'form': form})

def createtask(request):
	form = NewTaskForm(request.POST or None)

	context = {'form': form}

	print(context)

	# To see if the request method has post.
	if request.method != 'POST':
		print("It is not post")
		return render(request, 'createtask.html', context)

	# Check if the form is not valid them redirect to Home.html
	if not form.is_valid():
		return render(request, 'createtask.html', context)

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
	return redirect(response, 'home')

# Add note
def add_note(request, task_id):
	task = Task.objects.get(pk=task_id)
	notes = TaskNote.objects.filter(task__id=task_id)
	form = NoteForm(request.POST or None)

	if not request.method == "POST":
		return HttpResponseRedirect(f'/task/{task_id}')

	if not form.is_valid():
		return HttpResponseRedirect(f'/task/{task_id}')

	note = form.save(commit=False)
	note.task = task
	note.save()
	messages.success(request, "Noted!")
	return HttpResponseRedirect(f'/task/{task_id}')

def update_task(request, task_id):
	task = Task.objects.get(pk=task_id)
	form = DescForm(request.POST or None)

	if not request.method == "POST":
		return HttpResponseRedirect(f'/task/{task_id}')

	if not form.is_valid():
		print("The form is not valid")
		return HttpResponseRedirect(f'/task/{task_id}')

	form.desc = task.desc
	form.save()
	messages.success(request, "Updated!")
	return HttpResponseRedirect(f'/task/{task_id}')