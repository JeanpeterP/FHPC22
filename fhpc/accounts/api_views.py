from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json
from .models import Account
from .common.encoders import AccountEncoder, AccountSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class AccountListApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            # Validate password
            password = serializer.validated_data['password']
            try:
                validate_password(password)
            except ValidationError as e:
                return Response(
                    {'error': ', '.join(e.messages)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create the account object using create_user()
            account = Account.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=password,
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name']
            )

            return Response(
                AccountSerializer(account).data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )