from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('core2.urls')),
    path('',include('core2.urls')),
]
