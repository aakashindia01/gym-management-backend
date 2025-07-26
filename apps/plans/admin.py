from django.contrib import admin
from .models import Plan, MemberPlan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'max_users', 'max_staff', 'duration_months', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(MemberPlan)
class MemberPlanAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'name', 'duration_months', 'cost', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
