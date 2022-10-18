from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from acomodacoes.views import listar_acomodacoes, detalhe
# from clientes.views import criar_cliente, login, logout



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_acomodacoes,name='listar_acomodacoes'),
    path('detalhe/<int:acomodacao_id>/', detalhe),
    path('clientes/', include('clientes.urls'))
]