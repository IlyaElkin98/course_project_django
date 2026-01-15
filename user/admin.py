from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'avatar', 'phone_number', 'country']
    list_filter = ['id',]
    search_fields = ['username']
