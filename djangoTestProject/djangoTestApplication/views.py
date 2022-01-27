from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    context = {
        'item1': 'variables',
        'item2': 'estaticas'
    }
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies, 'context': context})

def register(request):
    return render(request, 'register.html')


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})