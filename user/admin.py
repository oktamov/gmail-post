from django.contrib import admin
from .models import UserForm1, UserForm2

# UserForm1 uchun mukammal admin paneli
class UserForm1Admin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'nationality', 'date', 'address', 'amount')
    search_fields = ('full_name', 'email', 'nationality')
    list_filter = ('nationality', 'date')
    date_hierarchy = 'date'

# UserForm2 uchun mukammal admin paneli
class UserForm2Admin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'email')
    search_fields = ('full_name', 'email')
    list_filter = ('role',)

# Modellarni admin panelida ro'yxatdan o'tkazish
admin.site.register(UserForm1, UserForm1Admin)
admin.site.register(UserForm2, UserForm2Admin)
