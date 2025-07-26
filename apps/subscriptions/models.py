from django.db import models
from apps.plans.models import MemberPlan

class MemberSubscription(models.Model):
    member = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='member_subscription')
    plan = models.ForeignKey(MemberPlan, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
