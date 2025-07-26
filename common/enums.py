from django.db import models

class Role(models.TextChoices):
    SUPER_ADMIN = 'Super Admin', 'Super Admin'
    TENANT_ADMIN = 'Tenant Admin', 'Tenant Admin'
    MANAGER = 'Manager', 'Manager'
    STAFF = 'Staff', 'Staff'
    MEMBER = 'Member', 'Member'


class Status(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    INACTIVE = 'Inactive', 'Inactive'
    PENDING = 'Pending', 'Pending'
    BLOCKED = 'Blocked', 'Blocked'

class Currency(models.TextChoices):
    INR = 'INR', 'Indian Rupee (INR)'
    USD = 'USD', 'US Dollar (USD)'
    EUR = 'EUR', 'Euro (EUR)'
    GBP = 'GBP', 'British Pound (GBP)'
    JPY = 'JPY', 'Japanese Yen (JPY)'
    AUD = 'AUD', 'Australian Dollar (AUD)'
    CAD = 'CAD', 'Canadian Dollar (CAD)'