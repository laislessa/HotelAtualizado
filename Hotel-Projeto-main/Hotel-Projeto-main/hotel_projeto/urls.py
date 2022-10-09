from django.contrib import admin
from django.urls import path
from acomodacoes.views import listar_acomodacoes, detalhe
# from clientes.views import criar_cliente, login, logout

app_name = 'clientes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_acomodacoes),
    path('detalhe/<int:acomodacao_id>/', detalhe),
    # path('cadastrar/', criar_cliente, name="criar_cliente"),
    # path('entrar/', login, name="login"),
    # path('sair/', logout, name="logout"),
]
