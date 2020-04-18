from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lead, name="lead"),
    path('lead/', views.lead, name="lead"),
    path('api/lead/', views.LeadListCreate.as_view() ),
]
