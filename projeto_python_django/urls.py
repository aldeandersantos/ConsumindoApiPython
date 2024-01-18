from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_enderecos/', include('app_enderecos.urls')),
]