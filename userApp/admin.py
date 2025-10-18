from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(BorrowersModel)
class BorrowersAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone"]