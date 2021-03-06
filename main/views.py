from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .forms import MentorForm
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from .decorators import allowed_users, unauthenticated_user


def is_student(user):
    return user.groups.filter(name='Students').exists()


def is_mentor(user):
    return user.groups.filter(name='Mentors').exists()


@login_required
@user_passes_test(is_mentor)
def MentorDashboard(request):
    return render(request, 'main/mentor.html')


@login_required
@user_passes_test(is_mentor)
def MentorRegister(request):
    return render(request, 'main/mentor_auth.html')


@login_required
@user_passes_test(is_mentor)
def MentorRegisterCourse(request):
    return render(request, 'main/course_reg.html')


@login_required
@user_passes_test(is_mentor)
def createCourse(request):
    return render(request, 'main/create_course.html')


def index(request):
    return render(request, 'main/new.html')


def celebrity(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/celebrity.html', {'title': 'Main page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Form is invalid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new_notes.html', context)


@allowed_users(allowed_roles=['Student'])
def find_mentor(request):
    error = ''
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:

            error = 'Form is invalid'
    form = MentorForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/mentorFind.html', context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def mentor(request):
    return render(request, 'main/mentor.html')


def mentor_auth(request):
    return render(request, 'main/mentor_auth.html')


def course_reg(request):
    return render(request, 'main/course_reg.html')


def create_course(request):
    return render(request, 'main/create_course.hmtl')
