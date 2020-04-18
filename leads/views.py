from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics
from decouple import config
from .forms import LeadForm
from .models import Lead
from .serializers import LeadSerializer

#Generic views work well to render the Rest API easy access pages
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

#View to render the Lead Form
def lead(request):
    gkey = config('GOOGLE_MAPS_API_KEY')
    leadForm = LeadForm()
    if request.method == "POST":
        leadForm = LeadForm(request.POST)
        if leadForm.is_valid():
            lead = leadForm.save(commit=False)
            lead.save()
            return render(request, 'thanks.html')
        else:
            leadForm = LeadForm()
    return render(request, 'lead.html', locals())
    