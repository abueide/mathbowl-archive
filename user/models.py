from django.db import models
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    pass

    # add additional fields in here
    teacher = models.BooleanField(default=False)

    # stats
    games = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)

    def __str__(self):
        return self.email
