from django.db import models
from django.utils import timezone
from account.models import Users

# Create your models here.

class Income(models.Model):
    source = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    