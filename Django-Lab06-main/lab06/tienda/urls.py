from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:producto_id>/', views.ProductoDetailView.as_view(), name='producto-detail'),


]
