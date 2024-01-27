from django.contrib import admin
from .models import Hashtag

# Register your models here.
@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
