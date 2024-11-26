from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_transacciones, name='lista_transacciones'),
    path('crear/', views.crear_transaccion, name='crear_transaccion'),
    path('editar/<int:pk>/', views.editar_transaccion, name='editar_transaccion'),
    path('eliminar/<int:pk>/', views.eliminar_transaccion, name='eliminar_transaccion'),
]
