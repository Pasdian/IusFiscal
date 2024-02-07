from django.contrib import admin
from efos_app.models import *

# Register your models here.


class EfoAdmin(admin.ModelAdmin):
    list_filter = ['fiscal_situation']
    list_display = ['rfc', 'fiscal_situation', 'modified']
    search_fields = ['rfc']
    fieldsets = [
        ('General Information', {'fields': [
         'rfc', 'social_reason', 'fiscal_situation']}),
        ('SAT presumption Information', {'fields': [
            'sat_presumtion_date', 'sat_presumtion_file_no', 'sat_presumtion_file_date',
            'sat_definitive_date', 'sat_definitive_file_no', 'sat_definitive_file_date',
            'sat_distorted_date', 'sat_distorted_file_no', 'sat_distorted_file_date',
            'sat_favorable_ruling_date', 'sat_favorable_ruling_file_no', 'sat_favorable_ruling_file_date',
        ]}),
        ('DOF presumption Information', {'fields': [
            'dof_presumtion_date', 'dof_presumtion_file_no', 'dof_presumtion_file_date',
            'dof_definitive_date', 'dof_definitive_file_no', 'dof_definitive_file_date',
            'dof_distorted_date', 'dof_distorted_file_no', 'dof_distorted_file_date',
            'dof_favorable_ruling_date', 'dof_favorable_ruling_file_no', 'dof_favorable_ruling_file_date',
        ]}),
    ]


admin.site.register(Efo, EfoAdmin)


class PersonDetailAdmin(admin.ModelAdmin):
    list_display = ['rfc', 'assumption', 'modified']
    list_filter = ['state', 'type_of_person', 'assumption', 'modified']
    search_fields = ['rfc']


admin.site.register(PersonDetail, PersonDetailAdmin)


class CancellationAdmin(admin.ModelAdmin):
    list_display = ['rfc', 'amount', 'date_published']
    list_filter = ['state', 'type_of_person', 'date_published']
    search_fields = ['rfc']


admin.site.register(Cancellation, CancellationAdmin)

class ReductionAdmin(admin.ModelAdmin):
    list_display = ['rfc', 'amount', 'date_published', 'authorization_date']
    list_filter = ['state', 'type_of_person', 'date_published', 'authorization_date']
    search_fields = ['rfc']

admin.site.register(Art74Reduction, ReductionAdmin)
