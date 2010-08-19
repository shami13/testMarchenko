from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import UserForm
from models import User


@login_required
def main_page(request):
    if len(request.POST) > 0:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        user = User.objects.latest('pk')
        form = UserForm(instance=user)
    form.fields.keyOrder.reverse()
    return render_to_response('main.html', {'form': form}, context_instance=RequestContext(request))
