from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    # all the api urls and config
    path("api/", include(("api.urls", "api"), namespace="create_tweet")),
]

admin.site.site_title = "twitter"
admin.site.index_title = "twitter"
admin.site.site_header = "twitter"
