"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.models import modelformset_factory
from django.forms import ModelForm
from django.forms.models import model_to_dict
from forms import *

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

def register(request):
    """Registration logic implemented here with access to request and cleaned data"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=str(cd['username']), email=str(cd['email']), password=str(cd['password1']))
            if cd['role']=='1':
                try:
                    techgroup = Group.objects.get(name='Technician')
                    user.groups.add(techgroup)
                except Exception as e:
                    techgroup = Group.objects.create(name='Technician')
                    user.groups.add(techgroup)
            if cd['role']=='2':
                try:
                    PIgroup = Group.objects.get(name='Principal Investigator')
                    user.groups.add(PIgroup)
                    user.save()
                    user = authenticate(username=request.POST['username'], password=request.POST['password1'])
                    login(request, user)
                    return HttpResponseRedirect('/interfact/labmgmt/add_PI/')
                except Exception as e:
                    PIgroup = Group.objects.create(name='Principal Investigator')
                    user.groups.add(PIgroup)
                    user.save()
                    user = authenticate(username=request.POST['username'], password=request.POST['password1'])
                    login(request, user)
                    return HttpResponseRedirect('/interfact/labmgmt/add_PI/')
            user.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/login')
def add_PI(request):
    if request.method == 'POST':
        form = PrincipalInvestigatorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            pi = PrincipalInvestigator(user_account=request.user, first_name=cd['first_name'], last_name=cd['last_name'],
                                       phone=cd['phone'], institution=cd['institution'])
            pi.save()
            return HttpResponseRedirect('/interfact/labmgmt/')
    else:
        form = PrincipalInvestigatorForm()
    return render(request, 'app/add_PI.html', {'form': form})

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/login')
def labmgmt(request):
    return render(request, 'app/labmgmt.html')

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/login')
def order(request):
    if request.method == 'POST':
        number_of_samples=int(request.POST.get('number_of_samples'))
        #Add this number of samples or sequencing run object to session?
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            o = Order(name=cd['name'], description=cd['description'], number_of_samples=cd['number_of_samples'])
            o.save()
            request.session['order'] = o.pk
            request.session['number_of_samples'] = number_of_samples
            return HttpResponseRedirect('/interfact/labmgmt/order/sample_details/')
    else:
        form = OrderForm()
    return render(request, 'app/order.html', {'form': form,})

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/login')
def sample_details(request):
    SampleFormSetFactory = modelformset_factory(Sample, form=ModelForm, fields=('sampleID', 'name', 'laboratory', 'organism', 'order'),
                                                extra=request.session.get('number_of_samples'))
    if request.method == 'POST':
        sampleformset=SampleFormSetFactory(request.POST, queryset=Sample.objects.none())
        if sampleformset.is_valid():
            for sampleform in sampleformset:
                cd = sampleform.cleaned_data
                orderkey = request.session['order']
                order=Order.objects.get(pk=orderkey)
                s = Sample(sampleID=cd['sampleID'], name=cd['name'], laboratory=cd['laboratory'], organism=cd['organism'],
                           order=order)
                s.save()
            return HttpResponseRedirect('/interfact/labmgmt/')
    else:
        sampleformset = SampleFormSetFactory(queryset=Sample.objects.none())
    return render(request, 'app/sample_details.html', {'sampleformset': sampleformset})

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/login')
def add_laboratory(request):
    if request.method == 'POST':
        form = LaboratoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            lab = Laboratory(name=cd['name'], principal_investigator=cd['principal_investigator'])
            lab.save()
            return HttpResponseRedirect('/interfact/labmgmt/')
    else:
        form = LaboratoryForm()
    return render(request, 'app/add_laboratory.html', {'form': form})

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/login')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request=request)
        if form.is_valid():
            cd = form.cleaned_data
            p = Project(projectID=cd['projectID'], name=cd['name'], description=cd['description'],
                        laboratory=cd['laboratory'])
            p.save()
            for sample in cd['samples']:
                p.samples.add(sample)
            # TODO instantiate Project
            return HttpResponseRedirect('/interfact/labmgmt/')
    else:
        form = ProjectForm(request=request)
    return render(request, 'app/add_project.html', {'form': form})

@user_passes_test(lambda u: u.groups.filter(name='Principal Investigator'), login_url='/login')
def add_organism(request):
    if request.method == 'POST':
        form = OrganismForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            o = Organism(common=cd['common'], linnaean=cd['linnaean'], strain=cd['strain'])
            o.save()
            return HttpResponseRedirect('/interfact/labmgmt/')
    else:
        form = OrganismForm()
    return render(request, 'app/add_organism.html', {'form': form})

@user_passes_test(lambda u: u.groups.filter(name='Technician'), login_url='/login')
def techdesk(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'app/techdesk.html')

def view_order(request):
    order_detail = request.session['order']
    query_results = Order.objects.filter()
    return render(request, 'app/view_order.html', {'query_results': query_results})

def view_sample(request):
    sample_detail = request.session['sample']
    query_results = Sample.objects.filter()
    return render(request, 'app/view_sample.html', {'query_results': query_results})

def view_project(request):
    project_detail = request.session['project']
    query_results = Project.objects.filter()
    return render(request, 'app/view_project.html', {'query_results': query_results})

def list_orders(request):
    #TODO show orders with their samples ?via related_name?
    #TODO have each record link to detailed view
    query_results = Order.objects.all()
    num = len(query_results)
    OrderFormSetFactory = modelformset_factory(Order, form=OrderForm, exclude=(), max_num=num)
    orderformset = OrderFormSetFactory()
    return render(request, 'app/list_orders.html', {'orderformset': orderformset})

def list_samples(request):
    #TODO display only samples associated with current user
    #TODO have each record link to detailed view
    query_results = Sample.objects.all()
    num = len(query_results)
    SampleFormSetFactory = modelformset_factory(Sample, form=ModelForm, fields=('sampleID', 'name', 'laboratory', 'organism', 'order'), max_num=num)
    sampleformset = SampleFormSetFactory()
    return render(request, 'app/list_samples.html', {'sampleformset': sampleformset})

def list_projects(request):
    #TODO handle issues with Form receiving request so current users projects will display
    #TODO have each record link to detailed view
    query_results = Project.objects.all()
    num = len(query_results)
    ProjectFormSetFactory = modelformset_factory(Project, form=ProjectForm, exclude=(), max_num=num)
    projectformset = ProjectFormSetFactory()
    return render(request, 'app/list_projects.html', {'projectformset': projectformset})

def receive_order(request):
    return render(request, 'app/receive_order.html', {'': None})

def add_pool(request):
    return render(request, 'app/add_pool.html', {'': None})

def update_status(request):
    return render(request, 'app/update_status.html', {'': None})

def list_pools(request):
    return render(request, 'app/list_pools.html', {'': None})