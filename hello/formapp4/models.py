from django.db import models


# Create your models here.
class Task(models.Model):
    class Meta:
        db_table='task'
        ordering = ['-text']

    text = models.TextField()

    def __str__(self):
        return f"{self.text}"
