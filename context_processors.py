import settings
def add_django_settings_to_request(request):
    return { 'django.settings' : settings }
