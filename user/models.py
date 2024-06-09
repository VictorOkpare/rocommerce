from django.db import models

class User(models.Model):
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   image= models.ImageField(blank=True)
   class Meta:
       ordering = ('name',)
    
# Create your models here.
