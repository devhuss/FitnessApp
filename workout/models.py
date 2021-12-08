from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.CharField(max_length=200)
    intensity = models.CharField(max_length=10)
    total_sets = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    bodyweight = models.PositiveIntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.workout


class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
