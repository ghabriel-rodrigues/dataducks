
#Chart/PDF dependencies
import json
import time
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.urls import path
from weasyprint import HTML

#Default import 
from django.contrib import admin

#Model dependencies
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets
from .models import Lead

# Class that represents the Lead entity in Admin and sets how this will be rendered there
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    #Function to transform querysets (data from search list) in PDF
    def generate_pdf(modeladmin, request, queryset):
        file_name = "report-{0}.pdf".format(time.strftime("%d-%m-%Y-%H-%M-%S"))
        html_string = render_to_string('reports/pdf.html', {'queryset': queryset})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(queryset));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(queryset)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(queryset)
            response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name)
            return response

        return response

    # Action to create PDF in admin (Lead list view)
    actions = ['generate_pdf']
    generate_pdf.label = "Generate PDF"
    generate_pdf.short_description = "Generate items selected as PDF"

    # Enables the google maps widget in admin
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
    
    # Rendering the page
    list_display = ['food', 'kindoffood', 
          'how_much_food','measure', 'how_many_ducks', 'fed_time',
          'fed_everyday', 'address']
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

    # Setting url to be used by chart in admin
    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        return extra_urls + urls

    # JSON endpoint for generating chart data that is used for dynamic loading via JS.
    def chart_data_endpoint(self, request):
        chart_data = self.chart_data()
        return JsonResponse(list(chart_data), safe=False)

    # Returning queryset to be rendered by chart in admin
    def chart_data(self):
        return (
            Lead.objects.values("how_many_ducks","fed_time")
            .order_by("-created_at")
        )


