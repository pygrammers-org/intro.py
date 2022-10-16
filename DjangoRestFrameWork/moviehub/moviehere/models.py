from django.db import models


# Create your models here.

class Movies(models.Model):
    """
    Movies Model

    Attributes:
        id (int): Id of movie,
        name (str): Movie name,
        year (date): Released movie date,
        description: Description of movie,
        created_at: Current Date and Time
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    year = models.DateField(null=True)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
