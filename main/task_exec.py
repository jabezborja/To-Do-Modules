# Imports
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from .models import Task, TaskNote
from .forms import NewTaskForm, NoteForm, DescForm
from django.contrib import messages


def done_task(request, task_id):
	task = Task.objects.get(id=task_id)
	post_archive = task.archived

	post_archive = True
	task.archived = post_archive
	task.save()

	messages.success(request, "Task archived!")
	return HttpResponseRedirect(reverse('home'))

def return_task(request, task_id):
	task = Task.objects.get(id=task_id)
	post_archive = task.archived

	post_archive = False
	task.archived = post_archive
	task.save()

	messages.success(request, "Task returned!")
	return HttpResponseRedirect(reverse('tasks_done'))

def delete_task(request, task_id):
	task = Task.objects.get(id=task_id)

	task.delete()
	messages.warning(request, "Task deleted!")
	return HttpResponseRedirect(reverse('tasks_done'))