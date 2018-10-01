from django import forms
from django.forms import ModelForm

from second.models import Organization


class OrgForm(ModelForm):
    class Meta:
        model = Organization
        fields = ('__all__')
