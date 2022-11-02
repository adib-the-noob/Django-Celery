from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('email','username','is_active','is_staff','is_superuser')
    list_filter = ('is_staff','is_superuser','is_active')
    fieldsets = (
        (None,{'fields':('email','username','password')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None,{'fields':('email','username','email','password1','password2')}),
    )
    search_fields = ('email','username')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User,UserAdmin)