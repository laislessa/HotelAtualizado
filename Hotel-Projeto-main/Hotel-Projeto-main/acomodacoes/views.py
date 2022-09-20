from django.shortcuts import render

from acomodacoes.models import Acomodacao,TipoAcomodacao

# Views criadas.


# Create your views here.
def listar_acomodacoes(request):
    acomodacoes = TipoAcomodacao.objects.all()
    return render(request, 'listar_acomodacoes.html', {'acomodacoes': acomodacoes})


def detalhe(request, acomodacao_id):
    acomodacoes = TipoAcomodacao.objects.get(pk=acomodacao_id)
    return render(request,'detalhe.html',{'acomodacao': acomodacoes[acomodacao_id]})
