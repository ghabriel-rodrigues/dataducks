from .models import Lead, Food, KindOfFood
from .serializers import LeadSerializer, FoodSerializer, KindOfFoodSerializer
from rest_framework import generics
from django.shortcuts import render, get_object_or_404

#Generic views work well to render the Rest API easy access pages
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class FoodListCreate(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class KindOfFoodListCreate(generics.ListCreateAPIView):
    queryset = KindOfFood.objects.all()
    serializer_class = KindOfFoodSerializer

#TODO: First, finish view, after, check material support and last but not least, convertion to react
def home(request):
    # lead = get_object_or_404(Lead)
    return render(request, 'home.html', locals())
    