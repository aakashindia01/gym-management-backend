from django.urls import path
from apps.tenants.views import TenantOnboardView


urlpatterns = [
    path('onboard-tenant/', TenantOnboardView.as_view(), name='onboard-tenant'),
]