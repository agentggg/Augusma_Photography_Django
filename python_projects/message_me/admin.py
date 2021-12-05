from django.contrib import admin
from .models import identity

# Register your models here.
@admin.register(identity)
class identity(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "number", "notes")
