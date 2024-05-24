from django.contrib import admin
from .models import Connect, Profile, CommonFlex


class ConnectModelAdmin(admin.ModelAdmin):
    ordering = ('date_uploaded', 'client')
    search_fields = ('client', 'job_title')


class ProfileAdmin(admin.ModelAdmin):
    ordering = ('hub_id',)
    search_fields = ('corper_name', 'video', 'hub_id')


class CommonFlexAdmin(admin.ModelAdmin):
    ordering = ('user',)
    search_fields = ('user','vibes',)


admin.site.register(Connect, ConnectModelAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(CommonFlex, CommonFlexAdmin)