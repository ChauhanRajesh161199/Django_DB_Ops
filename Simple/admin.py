from django.contrib import admin
from Simple.models import MyDB

# Register your models here.

class MyDBAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date", "phone")
  
admin.site.register(MyDB, MyDBAdmin)
