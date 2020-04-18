from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lead, name="lead"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),    
    path('api/lead/', views.LeadListCreate.as_view() ),
]
