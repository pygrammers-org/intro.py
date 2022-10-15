from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_movies),
    path('add/', views.add_movie),
    path('get-movie/<int:id>/', views.get_movie),
    path('delete/<int:id>/', views.delete_movie),
    path('update/', views.update_movie),
]
