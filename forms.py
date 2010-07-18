from django.contrib.admin import widgets
from django.forms import ModelForm
from models import User

class UserForm(ModelForm):
    class Meta:
        model = User
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['birthDate'].widget = widgets.AdminDateWidget()