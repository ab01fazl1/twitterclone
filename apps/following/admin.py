from django.contrib import admin
from .models import Relationship

# Register your models here.
@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ["from_user", "to_user", "status", "created_at"]
