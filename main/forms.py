from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Task, TaskNote

class NewTaskForm(forms.Form):
	title = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
	summary = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
	desc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'row justify-content-center'}))
	subject = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'display': 'flex'}))
	week_num = forms.IntegerField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'display': 'flex'}))


class NoteForm(forms.ModelForm):
	note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mt-3 mb-3', 'placeholder': 'Add notes here...', 'rows': '5', 'onkeyup': 'onChangeNote()', 'id': 'note'}), required=True)

	class Meta:
		model = TaskNote
		fields = ('note',)

class DescForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ('desc',)