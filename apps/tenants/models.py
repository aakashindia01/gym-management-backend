from django.db import models
import uuid


class Status(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    INACTIVE = 'Inactive', 'Inactive'
    PENDING = 'Pending', 'Pending'
    BLOCKED = 'Blocked', 'Blocked'

class Tenant(models.Model):
    tenantId = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tenantName = models.CharField(max_length=255)
    admin = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='tenant_admin')
    email = models.EmailField()
    phone = models.CharField(max_length=20) 
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    profilePicture = models.ImageField(upload_to='tenant_profiles/', null=True, blank=True)
    address = models.TextField()
    gstId = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.tenantName

