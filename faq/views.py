from django.shortcuts import render
from django.shortcuts import RequestContext


def faq(request):
    return render(request, 'faq/faq.html',
                  context_instance=RequestContext(request))
