from django.db import models

# Create your models here.

class registration(models.Model):
    uid = models.CharField(max_length=50)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    img = models.ImageField(upload_to='picture') 

class notice(models.Model):
    
    decleare = models.TextField()

class warning(models.Model):
    heading = models.CharField(max_length=50)
    decleare = models.TextField()

class eva(models.Model):
    faculty_name = models.CharField(max_length=100)
    faculty_id=  models.CharField(max_length=50)
    field1 = models.IntegerField()
    field2 = models.IntegerField()
    field3 = models.IntegerField()
    field4= models.IntegerField()
    field = models.IntegerField()
    comment = models.TextField()
    