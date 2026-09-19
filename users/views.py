from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    PlansSerializer,
    TransactoinSerializer,
    SendPaymentInfor,
)
from .models import Plans, TransActin
from dotenv import load_dotenv
import os
from .services import SandBoxPayment, sand_box_urls

User = get_user_model()
load_dotenv()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ListPlansView(ListAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
    permission_classes = [permissions.AllowAny]


class MyPlanView(ListAPIView):
    serializer_class = PlansSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Plans.objects.filter(users__id=self.request.user.id)


class ListTransactionsView(ListAPIView):
    serializer_class = TransactoinSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        transactions = TransActin.objects.filter(user=user)
        return transactions


# payment


class SendPaymentInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = SendPaymentInfor(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        plan = serializer.validated_data["plan_id"]
        amount = Plans.objects.get(id=plan.id).price
        payment = SandBoxPayment(sand_box_urls)

        description = "this is for get plan"
        call_back_url = "http://127.0.0.1:8000/accounts/payment/verify_payment/"
        metadata = {"email": user.email} if user.email else {}
        status, data = payment.send_information(
            os.getenv("MERCHAT_ID", ""), amount, description, call_back_url, metadata
        )
        if status:
            try:
                authority = data["data"]["authority"]
                transaction = TransActin(
                    user=user, price=amount, authority=authority, plane=plan
                )
                transaction.save()
                url = payment.redirect_to_zarinpal(data)
                return Response({"redirect_url": url}, status=200)
            except Exception as e:
                print(f"{e}")
                return Response({"message": "payment failed"}, status=400)
        return Response({"message": "payment failed"}, status=400)


class VerifyPaymentView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        authority = request.GET.get("Authority")
        status = request.GET.get("Status")
        if status == "OK":
            transaction = TransActin.objects.get(authority=authority)
            user = transaction.user
            amount = transaction.price
            merchat_id = os.getenv("MERCHAT_ID", "")
            data = {
                "merchant_id": merchat_id,
                "amount": amount,
                "authority": authority,
            }
            sandboxpayment = SandBoxPayment(sand_box_urls)
            status, data = sandboxpayment.verify(data)
            if status:

                if data["data"]["code"] == 100 or data["data"]["code"] == 101:
                    transaction.card_number = data["data"]["card_pan"]
                    transaction.fee = data["data"]["fee"]
                    transaction.save()
                    user.plan = transaction.plane
                    user.save()
                    return Response({"message": "payment successfuly"}, status=200)
                else:
                    return Response({"message": "payment failed1"}, status=400)

            else:
                return Response({"message": "payment failed2"}, status=400)
        else:
            return Response({"message": "payment failed3"}, status=400)
