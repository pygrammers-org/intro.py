from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .cbv import MoviesList, MoviesDetail

urlpatterns = [
    path('cbv/movies/', MoviesList.as_view()),
    path('cbv/movies/<int:pk>/', MoviesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)