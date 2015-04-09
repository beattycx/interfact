"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from registration_mod.forms import RegistrationForm
from app.models import *

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BootstrapRegistrationForm(RegistrationForm):
    """Registration form which uses bootstrap CSS."""
    pass

class OrderForm(forms.Form):
    sample_number = forms.CharField(max_length=96, widget=forms.NumberInput())
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    protocol = forms.ModelChoiceField(queryset=Protocol.objects.all())
    organism = forms.ModelChoiceField(queryset=Organism.objects.all())

class SampleDetailsForm(forms.Form):
    def __init__(self, number_of_fields, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        if number_of_fields:
            for i in range(0, number_of_fields):
                self.fields["Sample %d" % i] = forms.CharField(max_length=254, widget=forms.TextInput())
        else:
            pass
