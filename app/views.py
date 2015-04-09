"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from registration_mod.backends.simple.views import RegistrationView
from forms import *

class HomeRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/accounts/register/complete'

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def base(request):
    return render(request, 'app/base.html')

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/accounts/login')
def labmgmt(request):
    return render(request, 'app/labmgmt.html')

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/accounts/login')
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        return HttpResponseRedirect('/interfact/labmgmt/order/sample_details')
    else:
        form = OrderForm()
    return render(request, 'app/order.html', {'form': form})

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/accounts/login')
def sample_details(request):
    if request.method == 'POST':
        form = SampleDetailsForm(None, request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/interfact/labmgmt/')
    else:
        form = SampleDetailsForm(96)
    return render(request, 'app/sample_details.html', {'form': form})