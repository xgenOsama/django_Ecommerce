import re

from django.shortcuts import render, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import EmailConfirmed


# Create your views here.

def logout_view(request):
    logout(request)
    messages.info(request, "Successfly Logged out. feel free of <a href='%s'>login</a> again" % (reverse('auth_login')),
                  extra_tags='safe')
    return HttpResponseRedirect('%s' % (reverse('auth_login'),))


def login_view(request):
    form = LoginForm(request.POST or None)
    btn = "login"
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        # user.emailconfirmed.active_user_email()
        login(request, user)
        messages.success(request, "Successfly Logged in welcome back.")
        return HttpResponseRedirect('/')
    context = {
        "form": form,
        "btn": btn,
    }
    return render(request, "form.html", context)


def registeration_view(request):
    form = RegistrationForm(request.POST or None)
    btn = "join"
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.firstname = 'osama'
        new_user.save()
        messages.success(request, "Successfly Registered please confirm your email address now")
        return HttpResponseRedirect('/')
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)
        # login(request, user)
    context = {
        "form": form,
        "btn": btn,
    }
    return render(request, "form.html", context)


SHA1_RE = re.compile('^[a-f0-9]{40}$')


def activation_view(request, activation_key):
    print activation_key
    if SHA1_RE.search(activation_key):
        try:
            user_confirmed = EmailConfirmed.objects.get(activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            user_confirmed = None
            messages.error(request, "There is an error with your request")
            return HttpResponseRedirect('/')
        if user_confirmed is not None and not user_confirmed.confirmed:
            user_confirmed.confirmed = True
            page_message = "confirmation successful welcome"
            # user_confirmed.activation_key = "Confirmed"
            user_confirmed.save()
            messages.success(request, "Successfly Confirmed. please login")
        elif user_confirmed is not None and user_confirmed.confirmed:
            page_message = 'Already Confirmed'
            messages.success(request, "Already Confirmed.")
        else:
            page_message = ""
        context = {
            'page_message': page_message
        }
        return render(request, "accounts/activation_complete.html", context)
    else:
        raise Http404
