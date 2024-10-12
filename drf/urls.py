from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('api/account/', include('accounts.urls')),
    path('auth-api/', include('rest_framework.urls')),
]
