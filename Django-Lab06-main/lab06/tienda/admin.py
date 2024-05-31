from django.contrib import admin

# Registro de nuevos módulos al administrador.
from .models import Categoria
from .models import Producto

admin.site.register(Categoria)
admin.site.register(Producto)
