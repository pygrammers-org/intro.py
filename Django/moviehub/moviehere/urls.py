from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list-movies', views.list_movies, name="list_movies"),
    path('add-movie', views.add_movie, name="add_movie"),
    path('edit-movie/<int:movie_id>', views.edit_movie, name="edit_movie"),
    path('delete-movie/<int:movie_id>', views.delete_movie, name="delete_movie"),
]
