 
from django import forms
from django.forms import ModelForm

# Form dependencies
from captcha.fields import ReCaptchaField
from .models import Lead

# Determines how the form will be rendered to the user
class LeadForm(ModelForm):
    # Enables Recaptcha in LeadForm view
    # captcha = ReCaptchaField()

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
        