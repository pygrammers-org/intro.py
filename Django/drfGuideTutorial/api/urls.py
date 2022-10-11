from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/',views.addData),
    path('delete/<int:id>/',views.deleteData),
    path('update/<int:id>/',views.updateData),
]
