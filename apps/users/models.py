from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

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

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', Role.SUPER_ADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    memberId = models.CharField(max_length=20, unique=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
    phone = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profilePicture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    tenantId = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE, blank=True, null=True)
    tenantOwnerId = models.CharField(max_length=50, blank=True, null=True)
    addedOn = models.DateTimeField(default=timezone.now)
    addedBy = models.CharField(max_length=255, blank=True, null=True)
    isTempPasswordReset = models.BooleanField(default=False)
    subscriptionId = models.CharField(max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.memberId:
            role_prefix_map = {
                Role.SUPER_ADMIN: 'SUP',
                Role.TENANT_ADMIN: 'TEN',
                Role.MANAGER: 'MAN',
                Role.STAFF: 'STF',
                Role.MEMBER: 'MEM',
            }
            prefix  = role_prefix_map.get(self.role, 'MEM')
            last_user = User.objects.filter(role=self.role).order_by('-id').first()
            next_id = 1 if not last_user else last_user.id + 1
            self.memberId = f"{prefix}{str(next_id).zfill(4)}"
        super().save(*args, **kwargs)



    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email

