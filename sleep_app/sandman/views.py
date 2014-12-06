from django.template import RequestContext
from django.shortcuts import render_to_response
from json import dumps
#'dumps' isn't plural, actually is short for 'dump string'.  Same with 'loads'
from django.http import HttpResponse
from sandman.models import Mode
from sandman.models import Contacts
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    context = RequestContext(request)
    context_dict = {
        "sleep_mode": Mode.objects.all()[1],
        "user": Mode.objects.all()[0],
    }

    return render_to_response('sandman/index.html', context_dict, context)

@csrf_exempt
def ajax(request):

    if request.method == "POST":
        user = User()
        user.username = request.POST["name"]
        user.save()

    user = list(User.objects.all())
    user_list = []
    for u in user:
        user_list.append({
            "name": u.username
        })

    return HttpResponse(dumps(user_list, indent=4), content_type="application/json")

def dom(request):
    if request.method == "POST":
        print request.POST

    return render(request, 'sandman/dom.html')


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