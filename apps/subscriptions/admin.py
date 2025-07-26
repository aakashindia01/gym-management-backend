from django.contrib import admin
from .models import MemberSubscription

@admin.register(MemberSubscription)
class MemberSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('member', 'plan', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('member__username', 'plan__name')
