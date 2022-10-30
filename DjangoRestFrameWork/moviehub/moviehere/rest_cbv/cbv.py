from moviehere.models import Movies
from .serializers import MoviesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MoviesList(APIView):
    """
    List all Movies, or create a new movies.
    """
    def get(self, request, format=None):
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MoviesDetail(APIView):
    """
    Retrieve, update or delete a Movies instance.
    """
    def get_object(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movies = self.get_object(pk)
        serializer = MoviesSerializer(movies)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movies = self.get_object(pk)
        serializer = MoviesSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movies = self.get_object(pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)