from django.template import RequestContext
from django.shortcuts import render_to_response
from json import dumps
#'dumps' isn't plural, actually is short for 'dump string'.  Same with 'loads'
from django.http import HttpResponse
from sandman.models import Mode
from sandman.models import Help
from sandman.models import Contacts
from sandman.forms import HelpForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def register(request):
    if request.method == "POST":
        User.objects.create_user(request.POST["username"], None, request.POST["password"])
    return render(request, 'sandman/register.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                print("User is valid, active and authenticated")
                return redirect('/sandman/')
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            print("The username and password were incorrect.")
    return render(request, 'sandman/login.html')

def login_simple(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                return redirect('/sandman/')
        return render(request, 'sandman/login.html')

def index(request):
    context = RequestContext(request)
    context_dict = {
        # "sleep_mode": Mode.objects.all()[1],
        # "user": Mode.objects.all()[0],
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

def help(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            try:
                send_mail('subject', 'message', 'email', ["admin@sandman.com"])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/help/thanks/')
        else:
            return HttpResponse('Make sure all required fields are entered and valid.')

    return render_to_response('sandman/help.html')


def charmed(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('sandman/charmed.html', context_dict, context)


def settings(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('sandman/settings.html', context_dict, context)




#def track(request):

#def contact_list: