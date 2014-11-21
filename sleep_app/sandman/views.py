from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Sandman"}

    return render_to_response('sandman/index.html', context_dict, context)
    #using this template and context to respond to request

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Help"}
    return render_to_response('sandman/help.html', context_dict, context)
