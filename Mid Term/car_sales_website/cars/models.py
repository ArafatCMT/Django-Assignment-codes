from django.db import models
from datetime import datetime

# Create your models here.
class CarBrande(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    

class CarModel(models.Model):
    brand = models.ForeignKey(CarBrande, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.CharField(max_length=30)
    quentity = models.IntegerField()
    image = models.ImageField(upload_to='car_image')

    def __str__(self):
        return f'{self.model_name}'
    
class Comment(models.Model):
    post = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=10)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f'Commented by {self.name}'
