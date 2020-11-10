from django.contrib import admin
from django.urls import path
from main.views import home, tasks_done, taskview, sched
from main.task_exec import done_task, return_task, delete_task
from main.task_view import viewtask, add_note, update_task, createtask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('tasks_done', tasks_done, name="tasks_done"),
    path('task', taskview),
    path('task/<int:id>', viewtask),
    path('schedule',sched),

    path('createtask/', createtask),
    path('task/<int:task_id>/update_task', update_task, name="update_task"),
    path('task/<int:task_id>/add_note', add_note, name="add_note"),

    ###
    path('task/<int:task_id>/done', done_task, name="done_task"),
    path('task/<int:task_id>/return', return_task, name="return_task"),
    path('task/<int:task_id>/delete', delete_task, name="delete_task")
]