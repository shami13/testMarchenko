from django import template

register = template.Library()

@register.simple_tag
def edit_list(object):
    return '<a href="/admin/' + object._meta.app_label + '/' + object._meta.object_name + '/' + str(object.pk) +'"> edit ' + object._meta.object_name + '</a>' 