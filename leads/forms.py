 
from django import forms
from django.forms import ModelForm
from .models import Lead
from captcha.fields import ReCaptchaField
    

class LeadForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Lead

        exclude = ('created_at',)