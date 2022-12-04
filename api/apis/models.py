from django.db import models
# Create your models here.

class SuppliersModels(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

