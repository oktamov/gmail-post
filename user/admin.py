from django.contrib import admin
from .models import UserForm1, UserForm2


class UserForm1Admin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'nationality', 'date', 'address', 'amount')
    search_fields = ('full_name', 'email', 'nationality')
    list_filter = ('nationality', 'date')
    date_hierarchy = 'date'


class UserForm2Admin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'email')
    search_fields = ('full_name', 'email')
    list_filter = ('role',)


admin.site.register(UserForm1, UserForm1Admin)
admin.site.register(UserForm2, UserForm2Admin)
