from django.shortcuts import render, redirect
from moviehere.models import User


def index(request):
    return redirect('list_movies')


def list_movies(request):
    if request.method == 'GET':
        movies = User.objects.all()
        context = {'movies': movies}
        return render(request, 'list_movies.html', context)


def add_movie(request):
    if request.method == 'GET':
        return render(request, 'add_movie.html')
    if request.method == 'POST':
        movie = request.POST.get('moviename')
        director = request.POST.get('director')
        User.objects.create(movie_name=movie, director_name=director)
        return redirect('list_movies')
