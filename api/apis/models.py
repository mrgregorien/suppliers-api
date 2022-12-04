from django.db import models
# Create your models here.

class SuppliersModels(models.Model):
    name = models.CharField(max_length=50)
    type = model.CharField(max_length=12)
    website = models.CharField
    #category view spreadsheet scraped data
    
    def __str__(self):
        return self.name

