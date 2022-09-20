from django.contrib import admin
from .models import Acomodacao, TipoAcomodacao, Cliente

admin.site.register(TipoAcomodacao)
admin.site.register(Cliente)
admin.site.register(Acomodacao)
# Register your models here.
