from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ListPlansView, ListTransactionsView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("transactions/", ListTransactionsView.as_view(), name="transactions"),
    path("plans/", ListPlansView.as_view(), name="plans"),
]
