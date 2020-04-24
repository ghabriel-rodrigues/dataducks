
# PDF dependencies
import time
import uuid
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML

# Default import 
from django.contrib import admin

# Model dependencies
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets
from .models import Lead

# Class that represents the Lead entity in Admin and sets how this will be rendered there
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    #Function to transform querysets (data from search list) in PDF
    def generate_pdf(modeladmin, request, queryset):
        file_guid = uuid.uuid4()
        file_name = "report-{0}.pdf".format(time.strftime("%d-%m-%Y-%H-%M-%S"))
        html_string = render_to_string('reports/pdf.html', {'queryset': queryset})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(file_guid));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(file_guid)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(file_guid)
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


