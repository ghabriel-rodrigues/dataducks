# Rest dependencies
from rest_framework import generics
from .serializers import LeadSerializer

# View dependencies
from decouple import config
from django.shortcuts import render
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
    # App main process
    leadForm = LeadForm()
    if request.method == "POST":
        leadForm = LeadForm(request.POST)
        if leadForm.is_valid():
            lead = leadForm.save(commit=False)
            lead.save()
            return render(request, 'thanks.html')
        
    return render(request, 'lead.html', locals())

# Handling errors
def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
    