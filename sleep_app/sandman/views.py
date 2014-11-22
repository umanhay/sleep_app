from django.template import RequestContext
from django.shortcuts import render_to_response
from sandman.models import Mode, Contacts

def index(request):
    context = RequestContext(request)
    context_dict = {
        "sleep_mode": Mode.objects.all()[0]
    }

    return render_to_response('sandman/index.html', context_dict, context)


def charmed(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('sandman/charmed.html', context_dict, context)

def settings(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('sandman/settings.html', context_dict, context)

def help(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('sandman/help.html', context_dict, context)



#def track(request):

#def contact_list: