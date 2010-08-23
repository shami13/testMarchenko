from django.core.management.base import NoArgsCommand

def print_modles():
        from django.db.models import get_models
        models = get_models()
        result = ""
        for model in models:
            result += model._meta.object_name + " " + str(model.objects.count()) +"\n"
            for field in model._meta.fields:
                result += "\t" + field.name + " " + field.get_internal_type() +"\n"
        return result

class Command(NoArgsCommand):
    help = "Print for models for app"

    def handle_noargs(self, **options):
        print print_modles()
        