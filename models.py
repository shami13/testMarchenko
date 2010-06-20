from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    email = models.EmailField()