from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/media/uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"

class Owner(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_cars = models.ManyToManyField(Car)

    def __str__(self):
        return f"Owner: {self.owner}"