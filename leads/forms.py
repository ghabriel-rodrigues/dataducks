 
from django import forms
from django.forms import ModelForm

from decouple import config

# Form dependencies
from .models import Lead

# Determines how the form will be rendered to the user
class LeadForm(ModelForm):
    class Meta:
        model = Lead

        # Fields that will be excluded from the view
        exclude = ('geolocation','created_at',)

class LeadTestForm(ModelForm):
    # Disables Recaptcha in LeadForm test since it still has no component support
    # captcha = ReCaptchaField()

    class Meta:
        model = Lead

        # Fields that will be excluded from the view
        exclude = ('geolocation','created_at',)
        