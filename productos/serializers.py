"""
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'tipo', 'producto.imagen_url']

    def validate_precio(self, value):
        if value < 100:
            raise serializers.ValidationError('El precio no puede ser menor de 100 pesos.')
        return value
    
    def get_imagen_url(self, obj):
        request = self.context.get('request')
        if obj.imagen and hasattr(obj.imagen, 'url'):
            return request.build_absolute_uri(obj.imagen.url)
        return None


from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'tipo', 'imagen', 'imagen_url']

    def validate_precio(self, value):
        if value < 100:
            raise serializers.ValidationError('El precio no puede ser menor de 100 pesos.')
        return value
    

   
    def get_imagen_url(self, obj):
        request = self.context.get('request')
        if obj.imagen and hasattr(obj.imagen, 'url'):
            return request.build_absolute_uri(obj.imagen.url)
        return None
"""

from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'tipo', 'imagen']

    def validate_precio(self, value):
        if value < 100:
            raise serializers.ValidationError('El precio no puede ser menor de 100 pesos.')
        return value

       