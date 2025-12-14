from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navidad/', include('navidad.urls')),
    path('', include('navidad.urls')),  # Para que sea la página principal
]