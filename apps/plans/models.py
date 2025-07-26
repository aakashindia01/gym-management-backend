from django.db import models
import uuid

class Plan(models.Model):
    planId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_users = models.IntegerField()
    max_staff = models.IntegerField()
    duration_months = models.IntegerField()
    features = models.JSONField(default=dict)  # Optional: {"face_unlock": True, "whatsapp_billing": False}
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MemberPlan(models.Model):
    memberPlanId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration_months = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    services = models.JSONField(default=dict)  # e.g. {"personal_training": True, "locker": True}
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)