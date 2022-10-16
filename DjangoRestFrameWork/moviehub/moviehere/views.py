from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movies
from .serializers import MovieSerializer



# Create your views here.
@api_view(['GET'])
def list_movies(request):
    
    """
    List Movies
    --------------
    List Movies stored in the database.

    Args:
        request: <request object> [Get Method]

    Returns:
        response: <response object> [JSON]
    """

    movies = Movies.objects.all()
    serialized_movies = MovieSerializer(movies, many=True)
    return Response(serialized_movies.data)


@api_view(['GET'])
def get_movie(request, id):
    """
    Get Movie
    -------------
    Retrieve a Movie From Movies Table.

    Args:
        request: <request object> [Get Method]
        id: movie id
    Returns:
        response: <response object> [JSON]
    """
    try:
        Movies.objects.get(id=id)
        response = {'status': 'Available'}
        return Response(response)
    except Movies.DoesNotExist:
        response = {'status': 'NotAvailable'}
        return Response(response)



@api_view(['POST'])
def add_movie(request):
    """
    Add Movie
    -----------
    Insert A MovieDetails Data To Movies Table

    Args:
        request: <request object> [POST Method]
    Returns:
        response: <response object> [JSON]
    """
    print(request.data)
    serialized_movie = MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response({'status': 'okey'})


@api_view(['PUT'])
def update_movie(request):
    """
    Update Movie
    -----------
    Update Movie in Movies Table

    Args:
        request: <request object> [PUT Method]
    Returns:
        response: <response object> [JSON]
    """
    id = request.POST['id']
    try:
        movie = Movies.objects.get(id=id)
        serialized_movie = MovieSerializer(instance=movie, data=request.data)
        if serialized_movie.is_valid():
            serialized_movie.save()
            return Response(serialized_movie.data)
    except Movies.DoesNotExist:
        return Response({'status': 'failed to update'})


@api_view(['DELETE'])
def delete_movie(request, id):
    """
    Delete Movie
    -----------
    Delete Movie From Movies Table

    Args:
        request: <request object> [DELETE Method]
        id: movie id
    Returns:
        response: <response object> [JSON]
    """
    try:
        Movies.objects.get(id=id).delete()
        response = {'status': 'itemDeleted'}
        return Response(response)
    except Movies.DoesNotExist:
        response = {'status': 'itemNotAvailable'}
        return Response(response)



