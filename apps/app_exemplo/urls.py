from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'example'

urlpatterns = [
    path('create/', views.ClientesCreateView.as_view(), name='clientes-create'),
    path('<int:pk>/', views.ClientesDetailView.as_view(), name='clientes-detail'),    
    path('list/', views.ClientesListView.as_view(), name='clientes-list'),
    path('list/datatable/', views.ClientesListDatatableView.as_view(), name='clientes-list-datatable'),
    path('api-v1/list_json/', views.ClientesListJson.as_view(), name='clientes-list-json'),
    path('update/<int:pk>', views.ClientesUpdateView.as_view(), name='clientes-update'),
    path('delete/<int:pk>', views.ClientesDeleteView.as_view(), name='clientes-delete'),
    path('expiracao/', views.ClientesExpiracaoView.as_view(), name='clientes-expiracao'),
    path('aniversariantes/', views.ClientesAniversariantesView.as_view(), name='clientes-aniversariantes'),
    path('clientes/<int:cliente_id>/viagens/create/', views.ViagensCreateView.as_view(), name='viagens-create'),
    path('viagens/<int:pk>/', views.ViagensDetailView.as_view(), name='viagens-detail'),
    path('viagens/update/<int:pk>/', views.ViagensUpdateView.as_view(), name='viagens-update'),
    path('viagens/delete/<int:pk>/', views.ViagensDeleteView.as_view(), name='viagens-delete'),
    path('clientes/<int:cliente_id>/viagens/', views.ViagensListView.as_view(), name='viagens-list'),

]
