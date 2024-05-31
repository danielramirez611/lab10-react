from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('tienda.urls')),  # URLs de la aplicación 'tienda'
    path('admin/', admin.site.urls),  # URL de administración
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
