from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users, Projects, Tasks

class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    ('Extra Profile Info', {'fields': ('profile_image',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
    ('Extra Profile Info', {'fields': ('profile_image',)}),
    )

# Register your models here.
admin.site.register(Users, UserAdmin)
admin.site.register(Projects)
admin.site.register(Tasks)