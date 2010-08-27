def add_models_action(instance, action):
    from models import ModelActions
    if not isinstance(instance, ModelActions):
        model_actions = ModelActions()
        model_actions.model = instance._meta.verbose_name
        model_actions.action = action
        model_actions.save()


def add_models_action_save(instance, **kwargs):
    if instance.pk is None:
        add_models_action(instance, 'C')
    else:
        add_models_action(instance, 'M')


def add_models_action_delete(instance, **kwargs):
    add_models_action(instance, 'D')
