from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Car(models.Model):
    car_type = models.CharField(max_length=64)
    car_disc = models.TextField()
    driver = ForeignKey(get_user_model(), on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.car_type
