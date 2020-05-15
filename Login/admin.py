from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import normaluserform

class normaluserformInline(admin.TabularInline):
    model = normaluserform
    can_delete = False
    verbose_name_plural = 'normaluserform'

class UserAdmin(BaseUserAdmin):
    inlines = (normaluserformInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
