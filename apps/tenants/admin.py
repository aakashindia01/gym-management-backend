from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('tenantName', 'tenantId', 'email', 'phone', 'status')
    list_filter = ('status',)
    search_fields = ('tenantName', 'email', 'tenantId')