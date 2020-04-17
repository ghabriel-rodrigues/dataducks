from django.contrib import admin
from .models import Lead, Food, KindOfFood

admin.site.register(Lead)
admin.site.register(Food)
admin.site.register(KindOfFood)