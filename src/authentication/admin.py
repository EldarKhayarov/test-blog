from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # Менять дату регистрации и последнего входа нельзя
    readonly_fields = ('last_login', 'date_joined')

    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')


admin.site.register(User, UserAdmin)
