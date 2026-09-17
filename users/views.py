from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    PlansSerializer,
    TransactoinSerializer,
)
from .models import Plans, Transactin

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ListPlansView(ListAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
    permission_classes = [permissions.AllowAny]


class ListTransactionsView(ListAPIView):
    serializer_class = TransactoinSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        transactions = Transactin.objects.filter(user=user)
        return transactions
