from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('api/lead/', views.LeadListCreate.as_view() ),
    path('api/food/', views.FoodListCreate.as_view() ),
    path('api/kindoffood/', views.KindOfFoodListCreate.as_view() ),
]
