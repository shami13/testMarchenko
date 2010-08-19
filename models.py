from django.db import models
from django.db.models import signals
from signals import add_models_action_save, add_models_action_delete
from django.db.models.loading import get_apps, get_app
import settings

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    email = models.EmailField()
    birthDate = models.DateField()
    
class URL(models.Model):
    url = models.CharField(max_length=100)
    
ACTION_CHOICES = (
                  ('C', 'Created'),
                  ('M', 'Modified'),
                  ('D', 'Deleted'),
                  )
    
class ModelActions(models.Model):
    model = models.CharField(max_length=50)
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    date = models.DateTimeField(auto_now=True)

for app_name in settings.INSTALLED_APPS:
    if app_name.find("django") == -1:
        app = get_app(app_name)
        signals.pre_save.connect(add_models_action_save, sender=app.models)    
        signals.post_delete.connect(add_models_action_delete, sender=app.models)    