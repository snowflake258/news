from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.forms import UserChangeForm, UserCreateForm
from account.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('email', 'date_of_birth', 'is_superuser')
    list_filter = ('is_superuser',)
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_active')}),
        ('Личные данные', {'fields': ('date_of_birth',)}),
        ('Права доступа', {'fields': ('is_superuser', 'groups', 'user_permissions')})
    )

    filter_horizontal = ()


admin.site.register(User, UserAdmin)
