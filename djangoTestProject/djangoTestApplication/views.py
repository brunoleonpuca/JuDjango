from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movie, MovieCritic

# Create your views here.
def index(request):
    # context = {
    #     'item1': 'variables',
    #     'item2': 'estaticas'
    # }
    # 'context': context
    movies = MovieCritic.objects.all()
    return render(request, 'workspace/index.html', { 'movies': movies })

def goToHome(request):
    return redirect('/')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords does not match')
            return redirect('register')
    else:
        return render(request, 'auth/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User does not exist')
            return redirect('login')

    return render(request, 'auth/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount': amount_of_words})


# current_user = request.user.id
