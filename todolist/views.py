from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .forms import ToDoListForm
from .models import TodoList
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    # Render home screen
    return render(request, 'noted/home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'noted/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Save user to database
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                # Login user 
                login(request, user)
                return redirect('currentlist')
            except IntegrityError:
                error = 'That username has already been taken. Please choose a new username'
                return render(request, 'noted/signup.html', {'form': UserCreationForm(), 'error': error})
        else:
            return render(request, 'noted/signup.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'noted/login.html', {'form': AuthenticationForm(request.POST)})
    else:
        # Save user object if given credentials are valid
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            error = 'Username and password did not match'
            return render(request, 'noted/login.html', {'form': AuthenticationForm(), 'error': error})
        else:
            # Login user
            login(request, user)
            return redirect('currentlist')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def createlist(request):
    # Create new todo list
    if request.method == 'GET':
        return render(request, 'noted/create.html', {'form': ToDoListForm()})
    else:
        try:
            form = ToDoListForm(request.POST)
            """
            commit=False - save data in 'memory', not in database yet.
            It is because we get most of our model data from a form, 
            but we need to populate 'user' field with non-form data.
            """
            newtodo = form.save(commit=False)        
            # Add authenticated user to user column
            newtodo.user = request.user
            # Now save to database
            newtodo.save()
            return redirect('currentlist')
        except ValueError:
            return render(request, 'noted/create.html', {'form': ToDoListForm(), 'error': 'Error! Try again'})


@login_required
def currentlist(request):
    # View uncompleted tasks
    todo = TodoList.objects.filter(user=request.user, date_end__isnull=True)
    return render(request, 'noted/current.html', {'todo': todo})


@login_required
def completedlist(request):
    # View completed tasks
    todos = TodoList.objects.all().filter(user=request.user, date_end__isnull=False).order_by('date_end')
    return render(request, 'noted/completed.html', {'todos': todos})


@login_required
def viewlist(request, todo_pk):
    # Get object from database, if object does not exist return 404 error
    todo = get_object_or_404(TodoList, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        # Fill form fields with data from todo
        form = ToDoListForm(instance=todo)
        return render(request, 'noted/view.html', {'todo': todo, 'form': form})
    else:
        try:
            form = ToDoListForm(request.POST, instance=todo)
            form.save()
            return redirect('currentlist')
        except ValueError:
            return render(request, 'noted/view.html', {'todo': todo, 'form': form, 'error': 'Bad info'})


@login_required
def completelist(request, todo_pk):
    # Mark list as complete by adding data to 'date_end' field 
    todo = get_object_or_404(TodoList, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_end = timezone.now()
        todo.save()
        return redirect('currentlist')


@login_required
def deletelist(request, todo_pk):
    # Delete list
    todo = get_object_or_404(TodoList, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currentlist')
