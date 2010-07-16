from django.shortcuts import render_to_response
from django.template import RequestContext

from models import User
from forms import UserForm

def main_page(request):
    if len(request.POST) > 0:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    user = User.objects.latest('pk')
    form = UserForm(instance=user)
    return render_to_response('main.html', {'form': form}, context_instance=RequestContext(request))