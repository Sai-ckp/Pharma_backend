Sure, here's the contents for the file `/smartpharma_backend/smartpharma_backend/apps/accounts/admin.py`:

from django.contrib import admin
from .models import User  # Assuming you have a User model in models.py

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff')
    ordering = ('id',)