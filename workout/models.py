from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Workout(models.Model):
    # User model is created by Django. Instead of creating our own User model, we can simply use Django's user model.
    # the following line create a ForeignKey in your table
    # Since each user can have many todos, 1-to-many relationship is needed.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # complete = models.BooleanField(default=False)

    def __str__(self):
        return self.workout
