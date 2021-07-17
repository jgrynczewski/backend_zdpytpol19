from django.db import models
from django.urls import reverse

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} z {self.city} ({self.age})"

    def get_absolute_url(self):
        return reverse("classapp:hello")
