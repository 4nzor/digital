from django.contrib import admin

from second.models import Mapcheck, Flags, Organization, Question, About
import csv
from django.http import HttpResponse

admin.site.register(Mapcheck)


def export_orgs_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="organization.csv"'
    writer = csv.writer(response)
    writer.writerow(['country', 'owner_name', 'org_name', 'location'])
    organizations = queryset.all().values_list('country', 'owner_name', 'org_name', 'location')
    for organization in organizations:
        writer.writerow(organization)
    return response


export_orgs_csv.short_description = "Save as CSV"


@admin.register(Organization)
class OrgAdmin(admin.ModelAdmin):
    list_display = ['org_name', 'country', 'is_confirm']
    list_filter = ['country', 'is_confirm']
    list_per_page = 20
    save_as = True
    actions = [export_orgs_csv]



@admin.register(Question)
class QuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


admin.site.register(Flags)
admin.site.register(About)
