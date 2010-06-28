from models import User
from django.shortcuts import render_to_response


def main_page(request):
    if User.objects.count() > 0:
        user = User.objects.get()
    else:
        user = User()
        user.firstName = 'Mykhailo'
        user.lastName = 'Marchenko'
        user.bio = 'to be, or not to be'
        user.email = 'shami13@gmail.com'
        user.save()
    return render_to_response('main.html', {'customer': user})