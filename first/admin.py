from django.contrib import admin

# Register your models here.
from first.models import Account, Platform, Org, App, CMS

admin.site.register(Account)
admin.site.register(Org)
admin.site.register(Platform)
admin.site.register(App)
admin.site.register(CMS)
