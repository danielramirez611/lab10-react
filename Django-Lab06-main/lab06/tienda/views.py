from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class IndexView(APIView):
    def get(self, request):
        product_list = Producto.objects.order_by('nombre')[:6]
        categorias = Categoria.objects.all()
        productos = Producto.objects.all()
        categoria_id = request.GET.get('categoria')

        if categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            productos = productos.filter(categoria=categoria)

        categoria_serializer = CategoriaSerializer(categorias, many=True)
        producto_serializer = ProductoSerializer(productos, many=True)

        context = {
            'categorias': categoria_serializer.data,
            'productos': producto_serializer.data,
            'product_list': product_list, 
            'titulo': "Ecommerce Ramirez"
        }
        return Response(context)
    
    def post(self, request):
        # Your POST logic here
        pass

class ProductoListView(APIView):  # Adding ProductoListView class
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class ProductoDetailView(APIView):
    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        producto_serializer = ProductoSerializer(producto)
        return Response(producto_serializer.data)

    def put(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
