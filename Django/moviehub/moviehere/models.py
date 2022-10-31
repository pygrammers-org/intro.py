from django.db import models


class User(models.Model):
    movie_name = models.CharField(max_length=60)
    director_name = models.CharField(max_length=60)
