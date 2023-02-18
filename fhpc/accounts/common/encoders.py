from .json import ModelEncoder
from accounts.models import Account, Pet
from rest_framework import serializers

class AccountDetailEncoder(ModelEncoder):
    model = Account
    properties = ["username", "email", "first_name", "last_name", "is_staff", "zip_code"]

class AccountEncoder(ModelEncoder):
    model = Account
    properties = ["username", "email", "password", "first_name", "last_name"]

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["username", "email", "password", "first_name", "last_name"]