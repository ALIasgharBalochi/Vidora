from django.db import models
from django.contrib.auth.models import AbstractUser


class Plans(models.Model):
    plane_choises = [("br", "Bronze"), ("sl", "Silver"), ("gl", "Gold")]
    plane_name = models.CharField(choices=plane_choises)
    price = models.FloatField()

    def __str__(self):
        return self.plane_name


class CustomUser(AbstractUser):
    plan = models.ForeignKey(
        Plans, on_delete=models.PROTECT, null=True, blank=True, related_name="users"
    )


class Transactin(models.Model):
    price = models.FloatField()
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="transactions"
    )
    plane = models.ForeignKey(
        Plans,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transactions",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
