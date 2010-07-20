from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list

from forms import UserForm
from models import User, URL


@login_required
def main_page(request):
    if len(request.POST) > 0:
        form = UserForm(request.POST)
        form.save()
    else:
        user = User.objects.latest('pk')
        form = UserForm(instance=user)
    form.fields.keyOrder.reverse()
    return render_to_response('main.html', {'form': form}, context_instance=RequestContext(request))

def url_list(request):
    url_lists = URL.objects.all()[:10]
    return render_to_response('urllist.html',
        {'object_list': url_lists}, context_instance=RequestContext(request))
