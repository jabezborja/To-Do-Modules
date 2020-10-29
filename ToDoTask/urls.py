"""ToDoTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import home, viewtask, done_task, tasks_done, return_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('tasks_done', tasks_done, name="tasks_done"),
    path('task/<int:id>', viewtask),
    path('task/<int:task_id>/done', done_task, name="done_task"),
    path('task/<int:task_id>/return', return_task, name="return_task"),
    path('task/<int:task_id>/delete', delete_task, name="delete_task")
]
