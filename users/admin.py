from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (
            "프로필",
            {
                "fields": ("username", "password", "name", "email", "is_host", "avatar",),
            },
        ),
        (
            "퍼미션",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",

                ),
                "classes": ("collapse",),
            },

        ),
        (
            "중요정보",
            {
                "fields": ("last_login", "date_joined",),
                "classes": ("collapse",),
            },

        ),
    )

    list_display = ("username", "email", "name", "is_host",)
