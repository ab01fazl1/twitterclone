from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # simple jwt token urls
    # TODO move these into the api and combine them with the login feature
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # all the api urls and config
    path("api/", include(("api.urls", "api"), namespace="create_tweet")),
]

admin.site.site_title = "twitter"
admin.site.index_title = "twitter"
admin.site.site_header = "twitter"
