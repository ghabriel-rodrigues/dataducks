# Rest dependencies
from rest_framework import generics
from .serializers import LeadSerializer

# View dependencies
import urllib
import json

from decouple import config
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LeadForm
from .models import Lead

#Generic views work well to render the Rest API easy access pages
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

#View to render the Lead Form
def lead(request):
    # Needed to render the gmaps
    gkey = config('GOOGLE_MAPS_API_KEY')
    gcaptchakey = config('RECAPTCHA_PUBLIC_KEY')
    recaptchaError=''
    # App main process
    leadForm = LeadForm()
    if request.method == "POST":
        leadForm = LeadForm(request.POST)
        if leadForm.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            if recaptcha_response != '':
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': config('RECAPTCHA_PRIVATE_KEY'),
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req =  urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                ''' End reCAPTCHA validation '''
                if result['success']:
                    lead = leadForm.save(commit=False)
                    lead.save()
                    recaptchaError = False
                    return render(request, 'thanks.html')
                else:
                    recaptchaError = 'Invalid reCAPTCHA'
            else:
                recaptchaError = 'Invalid reCAPTCHA'
        else:
            recaptchaError = 'Some form fields are missing, please check the data'

        
    return render(request, 'lead.html', locals())

# Handling errors
def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
    