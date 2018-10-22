from django.contrib import admin
import xlwt
from second.models import Mapcheck, Flags, Organization, Question, About
import csv
from django.http import HttpResponse
import xlwt
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


def export_xls(modeladmin, request, queryset):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Data.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Dump")

    row_num = 0

    columns = [
        (u"ID", 2000),
        (u"Country", 6000),
        (u"Owner Name", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:
        row_num += 1
        row = [
            obj.pk,
            obj.country,
            obj.owner_name,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


export_xls.short_description = u"Export XLS"

@admin.register(Organization)
class OrgAdmin(admin.ModelAdmin):
    list_display = ['org_name', 'country', 'is_confirm']
    list_filter = ['country', 'is_confirm']
    list_per_page = 20
    save_as = True
    actions = [export_orgs_csv,export_xls]



@admin.register(Question)
class QuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


admin.site.register(Flags)
admin.site.register(About)
