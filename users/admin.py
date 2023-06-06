from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CudtomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'last_login',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'is_superuser',
        'date_joined'
    ]
    list_filter = (
        'id',
        'last_login',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'is_superuser',
        'date_joined'
    )
    search_fields = ('id', 'email', 'first_name', 'last_name')
