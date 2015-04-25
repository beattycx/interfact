"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *
from registration.users import UserModel

class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'

    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(label=_("E-mail"))
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=_("Password (again)"))
    role = forms.ChoiceField(label='Role', widget=forms.RadioSelect(attrs={'class': 'role'}), choices=(('1', 'Technician'), ('2', 'Principal Investigator')))

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = UserModel().objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data

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

class LaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        exclude = ()

class OrganismForm(forms.ModelForm):
    class Meta:
        model = Organism
        exclude = ()

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('samples',)

class PrincipalInvestigatorForm(forms.ModelForm):
    class Meta:
        model = PrincipalInvestigator
        exclude = ('user_account',)

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['laboratory'].queryset = Laboratory.objects.filter(principal_investigator=PrincipalInvestigator.objects.filter(user_account=self.request.user))
        self.fields['samples'].queryset = Sample.objects.filter(laboratory=Laboratory.objects.filter(principal_investigator=PrincipalInvestigator.objects.filter(user_account=self.request.user)))