from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register the User model in the Django admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    # Fields to display in admin list view
    list_display = ("username", "email", "phone", "role", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone', 'address')}),
    )