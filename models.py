from django.db import models
from django.db.models import signals
from signals import add_models_action_save, add_models_action_delete
from django.db.models.loading import get_models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    email = models.EmailField()
    birthDate = models.DateField()
    
class URL(models.Model):
    url = models.CharField(max_length=100)
    priority = models.IntegerField(default=1)
ACTION_CHOICES = (
                  ('C', 'Created'),
                  ('M', 'Modified'),
                  ('D', 'Deleted'),
                  )
    
class ModelActions(models.Model):
    model = models.CharField(max_length=50)
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    date = models.DateTimeField(auto_now=True)

for model in get_models():
    if model.__module__.find("django") == -1:
        signals.pre_save.connect(add_models_action_save, sender=model)    
        signals.post_delete.connect(add_models_action_delete, sender=model)    
