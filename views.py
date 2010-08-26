from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import UserForm
from models import User, URL
from django.utils import simplejson
from django.http import HttpResponse


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

def url_list(request):
    url_lists = URL.objects.all()[:10]
    return render_to_response('urllist.html',
        {'object_list': url_lists}, context_instance=RequestContext(request))

@login_required
def ajax_request(request):
    form = UserForm(request.POST)
    clean = form.is_valid()
    rdict = {'bad' : 'false'}
    if not clean:
        rdict.update({'bad':'true'})
        d = {}
        for e in form.errors.iteritems():
            d.update({e[0]:unicode(e[1])})
        rdict.update({'errs':d})
    else:
        form.save()
    json = simplejson.dumps(rdict)
    return HttpResponse(json, mimetype='application/javascript')
