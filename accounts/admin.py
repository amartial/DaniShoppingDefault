from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
from .models import Account

# Register your models here.

class AccountAdmin(ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined', 'password')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()

admin.site.register(
    Account,
    AccountAdmin
)
