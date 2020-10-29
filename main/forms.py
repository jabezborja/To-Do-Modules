from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Task, TaskNote

class NewTaskForm(forms.Form):
	title = forms.CharField(required=True)
	desc = forms.CharField(widget=CKEditorWidget)
	summary = forms.CharField(required=True)
	subject = forms.CharField(required=True)
	week_num = forms.IntegerField(required=True)

class NoteForm(forms.ModelForm):
	note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mt-3 mb-3', 'placeholder': 'Add notes here...', 'rows': '5', 'onkeyup': 'onChangeNote()'}), required=True)

	class Meta:
		model = TaskNote
		fields = ('note',)