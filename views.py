from models import User
from django.shortcuts import render_to_response


def main_page(request):
    user_list = list(User.objects.all())
    if len(user_list) > 0:
        user = user_list[0]
    else:
        user = User()
        user.firstName = 'Mykhailo'
        user.lastName = 'Marchenko'
        user.bio = 'to be, or not to be'
        user.email = 'shami13@gmail.com'
        user.save()
    return render_to_response('main.html', {'customer': user})