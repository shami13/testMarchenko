from django.shortcuts import render_to_response
from django.template import RequestContext

from models import User
from forms import UserForm

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
    form = UserForm(instance=user)
    return render_to_response('main.html', {'form': form}, context_instance=RequestContext(request))

def save(request):
    form = UserForm(request.POST)
    form.save()
    return render_to_response('main.html', {'form': form}, context_instance=RequestContext(request))
