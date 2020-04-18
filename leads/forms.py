 
from django import forms
from django.forms import ModelForm
from .models import Lead
from captcha.fields import ReCaptchaField
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class LeadForm(ModelForm):
    captcha = ReCaptchaField()
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

    class Meta:
        model = Lead
        exclude = ('geolocation','created_at',)