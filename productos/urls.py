from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet
from . import views

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('listar/', views.listar_productos, name='listar_productos'),
]
