from django.urls import path
from .models import SuperAdminRegisterView, TenantAdminRegisterView, StaffRegisterView, MemberRegisterView

urlpatterns = [
    path('register/superadmin/', SuperAdminRegisterView.as_view()),
    path('register/tenantadmin/', TenantAdminRegisterView.as_view()),
    path('register/staff/', StaffRegisterView.as_view()),
    path('register/member/', MemberRegisterView.as_view()),
]