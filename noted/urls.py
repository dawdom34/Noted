"""noted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # ToDoList

    # Home view
    path('', views.home, name='home'),
    # Create new list
    path('create/', views.createlist, name='createlist'),
    # View uncompleted tasks
    path('current/', views.currentlist, name='currentlist'),
    # View completed tasks
    path('completed/', views.completedlist, name='completedlist'),
    # View details about task
    path('todolist/<int:todo_pk>', views.viewlist, name='viewlist'),
    # Mark list as complete
    path('todolist/<int:todo_pk>/complete', views.completelist, name='completelist'),
    # Delete list
    path('todolist/<int:todo_pk>/delete', views.deletelist, name='deletelist'),
]
