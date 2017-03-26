from django.contrib import admin
from metrics_collector.models.container import RancherContainer
from metrics_collector.models.host import RancherHost
# Register your models here.

class RancherContainerAdmin(admin.ModelAdmin):
    list_display = ('host',)

admin.site.register(RancherContainer, RancherContainerAdmin)

class RancherHostAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(RancherHost, RancherHostAdmin)