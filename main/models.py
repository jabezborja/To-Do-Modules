from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

SUBJECTS = (
	('TLE','TLE'),
	('MATH','Mathematics'),
	('ENGLISH','ENGLISH'),
	('FILIPINO','FILIPINO'),
	('MAPEH','MAPEH'),
	('SCIENCE','SCIENCE'),
	('ESP','ESP'),
	('AP','Araling Panlipunan')
)

def x_ago_helper(diff):
	if diff.days > 0:
		return f'{diff.days} days ago'
	if diff.seconds == 0 or diff.seconds == 1:
		return 'Just Now'
	if diff.seconds < 60:
		return f'{diff.seconds} seconds ago'
	if diff.seconds < 3600:
		return f'{diff.seconds // 60} minutes ago'
	return f'{diff.seconds // 3600} hours ago'


class Task(models.Model):
	title = models.CharField(max_length=200)
	desc = RichTextField(blank=True, null=True)
	summary = RichTextField(blank=True, null=True)
	archived = models.BooleanField(default=False)
	subject = models.CharField(choices=SUBJECTS, max_length=50, default='TLE')
	week_num = models.IntegerField()
	created = models.DateTimeField(editable=False)
	modified = models.DateTimeField()

	def x_ago(self):
		diff = timezone.now() - self.created
		return x_ago_helper(diff)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Task, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class TaskNote(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	note = models.TextField()
	created = models.DateTimeField(editable=False)
	modified = models.DateTimeField()
	hidden = models.BooleanField(default=False)

	def x_ago(self):
		diff = timezone.now() - self.created
		return x_ago_helper(diff)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(TaskNote, self).save(*args, **kwargs)

	def __str__(self):
		return self.note
		