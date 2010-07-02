from django.shortcuts import render_to_response
from django.template import RequestContext
from models import User


def main_page(request):
    if User.objects.count() > 0:
        user = User.objects.latest('pk')
    else:
        user = User()
        user.firstName = 'Mykhailo'
        user.lastName = 'Marchenko'
        user.bio = 'to be, or not to be'
        user.email = 'shami13@gmail.com'
        user.save()
    return render_to_response('main.html', {'customer': user}, context_instance=RequestContext(request))
