from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    if request.user.is_authenticated():
        template = 'homepages/home.html'
    else:
        template = 'homepages/index.html'
    return render_to_response(template,
                              context_instance=RequestContext(request))
