from django.urls import path, include
from .api_views import(
    #api_accounts,
    AccountListApiView,
)

urlpatterns=[
    #path("accounts/", api_accounts, name="api_salespersons")
    path('accounts/', AccountListApiView.as_view()),
]