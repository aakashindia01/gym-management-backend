from django.urls import path
from .views import SuperAdminRegisterView, TenantAdminRegisterView, StaffRegisterView, ManagerRegisterView, MemberRegisterView, TokenSerializer

urlpatterns = [
    path('register/superadmin', SuperAdminRegisterView.as_view()),
    path('register/tenantadmin', TenantAdminRegisterView.as_view()),
    path('register/staff', StaffRegisterView.as_view()),
    path('register/manager', ManagerRegisterView.as_view()),
    path('register/member', MemberRegisterView.as_view()),
    path('login', TokenSerializer.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenSerializer.as_view(), name='token_refresh'),
]