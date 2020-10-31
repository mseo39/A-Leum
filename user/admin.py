from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(UserAdmin):
    """ Consumer User Admin """

    fieldsets = (
        (
            "Consumer Profile",
            {
                "fields": (
                    "name",
                    "gender",
                    "age",
                    "phone",
                )
            },
        ),
    )

    list_display = ("name","gender","age","phone")