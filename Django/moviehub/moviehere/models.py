from django.db import models

# Create your models here.

class Movies(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    year = models.DateField(null=True)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_id(self):
        return self.id

