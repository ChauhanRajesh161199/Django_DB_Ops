from django.contrib import admin
from Simple.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "created_at")
  
admin.site.register(User, UserAdmin)
