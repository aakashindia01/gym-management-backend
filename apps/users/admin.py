from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin 

# Change admin site header
admin.site.site_header = "FitVerse Gym Management Admin"

# Change browser tab title
admin.site.site_title = "FitVerse Admin Portal"

# Change index title (dashboard main page)
admin.site.index_title = "Welcome to FitVerse Gym Management System"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('memberId', 'name', 'role', 'status', 'tenantId', 'addedOn')
    list_filter = ('role', 'status', 'tenantId')
    search_fields = ('email', 'name', 'memberId', 'phone')
    ordering = ('-addedOn',)

