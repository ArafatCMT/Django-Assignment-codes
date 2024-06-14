from django.db import models

# Create your models here.
class Order(models.Model):
    carID = models.IntegerField()
    userID = models.IntegerField()

    def __str__(self):
        return f'carID {self.carID} buy by userId {self.userID}'
