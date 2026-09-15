from django.contrib import admin
from .models import Plans, CustomUser

# Register your models here.


@admin.register(Plans)
class AdminPlan(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    pass
