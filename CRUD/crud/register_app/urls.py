from django.urls import path
from .views import registro_list, registro_create, registro_update, registro_delete

urlpatterns = [
    path('registros/', registro_list, name='registro-list'),
    path('registros/create/', registro_create, name='registro-create'),
    path('registros/<int:pk>/update/', registro_update, name='registro-update'),
    path('registros/<int:pk>/delete/', registro_delete, name='registro-delete'),
]
