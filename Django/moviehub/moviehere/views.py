from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movies
from .serializers import MovieSerializer

from datetime import datetime


# Create your views here.
@api_view(['GET'])
def list_all_movies(request):
    movies = Movies.objects.all()
    serialized_movies = MovieSerializer(movies, many=True)
    return Response(serialized_movies.data)


@api_view(['POST'])
def add_movie(request):
    serialized_movie = MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response({'status': 'okey'})


@api_view(['DELETE'])
def delete_movie(request, id):
    try:
        Movies.objects.get(id=id).delete()
        response = {'status': 'itemDeleted'}
        return Response(response)
    except Movies.DoesNotExist:
        response = {'status': 'itemNotAvailable'}
        return Response(response)


@api_view(['GET'])
def get_movie(request, id):
    try:
        Movies.objects.get(id=id)
        response = {'status': 'Available'}
        return Response(response)
    except Movies.DoesNotExist:
        response = {'status': 'NotAvailable'}
        return Response(response)


@api_view(['PUT'])
def update_movie(request):
    id = request.POST['id']
    try:
        movie = Movies.objects.get(id=id)
        serialized_movie = MovieSerializer(instance=movie, data=request.data)

        if serialized_movie.is_valid():
            serialized_movie.save()
            return Response(serialized_movie.data)
    except Movies.DoesNotExist:
        return Response({'status': 'failed to update'})
