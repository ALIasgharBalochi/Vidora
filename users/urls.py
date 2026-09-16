from django.urls import path
from .views import RegisterView, LoginView, ListPlansView, ListTransactionsView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("transactions/", ListTransactionsView.as_view(), name="transactions"),
    path("plans/", ListPlansView.as_view(), name="plans"),
]
