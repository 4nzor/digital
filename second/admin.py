from django.contrib import admin

from second.models import Mapcheck, Flags , Organization , C0untry , Question

admin.site.register(Mapcheck)
admin.site.register(Organization)
admin.site.register(C0untry)
@admin.register(Question)
class QuestAdmin(admin.ModelAdmin):
    list_display = ['name' , 'status']
admin.site.register(Flags)
