from django.db import models
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import AbstractUser, Permission, Group
# Create your models here.

class Account(AbstractUser):
    zip_code = models.CharField(max_length=15)

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='account_user_permissions'
    )

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='accounts_groups'
    )
    
    def get_api_url(self):
        return reverse("api_accounts", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username


class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    owner = models.ForeignKey(
        Account, 
        related_name="pets", 
        on_delete=models.CASCADE
        )

