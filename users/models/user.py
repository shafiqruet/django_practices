from django.db import models
from django.contrib import admin


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    sponsor_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class UserAdmin(admin.ModelAdmin):
    search_fields = "first_name"
    empty_value_display = "-empty-"
    list_display = ["first_name"]
