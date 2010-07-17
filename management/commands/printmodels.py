from django.core.management.base import AppCommand

def print_modles(app):
        from django.db.models import get_models
        models = get_models(app)
        result = ""
        for model in models:
            result += model._meta.object_name + " " + str(model.objects.count()) +"\n"
            for field in model._meta.fields:
                result += "\t" + field.name + " " + field.get_internal_type() +"\n"
        return result

class Command(AppCommand):
    help = "Print for models for app"
    args = "[appname ...]"

    def handle_app(self, app, **options):
        print print_modles(app)
        