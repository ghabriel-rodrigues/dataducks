from django.contrib import admin
from .models import Lead
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import Trunc
from django.http import JsonResponse
from django.urls import path


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        pass
        # queryset.update(status='p')
    make_published.short_description = "Mark selected stories as published"

    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
    list_display = ['food', 'kindoffood', 
          'how_much_food','measure', 'how_many_ducks', 'fed_time',
          'fed_everyday', 'address', 'created_at']
    list_filter = ('food', 'kindoffood', 
          'how_much_food','measure', 'how_many_ducks', 'fed_time',
          'fed_everyday', 'address', 'created_at')
    search_fields = ['email', 'kindoffood', 'food', 
          'how_much_food','measure', 'how_many_ducks', 'fed_time',
          'fed_everyday', 'address', 'created_at']

    ordering = ("-created_at",) 


     # Inject chart data on page load in the ChangeList view
    def changelist_view(self, request, extra_context=None):
        chart_data = self.chart_data()
        
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)

        extra_context = extra_context or {"chart_data": as_json}
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        # NOTE! Our custom urls have to go before the default urls, because they
        # default ones match anything.
        return extra_urls + urls

    # JSON endpoint for generating chart data that is used for dynamic loading
    # via JS.
    def chart_data_endpoint(self, request):
        chart_data = self.chart_data()
        return JsonResponse(list(chart_data), safe=False)

    def chart_data(self):
        return (
            Lead.objects.values("how_many_ducks","fed_time")
            .order_by("-created_at")
        )


