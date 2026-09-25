from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    RegisterView,
    ListPlansView,
    ListTransactionsView,
    SendPaymentInfoView,
    VerifyPaymentView,
    MyPlanView,
    CancelPlan,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("transactions/", ListTransactionsView.as_view(), name="transactions"),
    path("plans/", ListPlansView.as_view(), name="plans"),
    path("my_plan/", MyPlanView.as_view(), name="my_plan"),
    path("cancel_plan/", CancelPlan.as_view(), name="cancel_plane"),
    path(
        "payment/send_payment_info/",
        SendPaymentInfoView.as_view(),
        name="send_payment_info",
    ),
    path("payment/verify_payment/", VerifyPaymentView.as_view(), name="verify_payment"),
]
