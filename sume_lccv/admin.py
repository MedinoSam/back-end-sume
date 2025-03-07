from django.contrib import admin
from .models import Projetos, Colaboradores, Financiadores, AreasTecnologicas

admin.site.register(Projetos)
admin.site.register(Colaboradores)
admin.site.register(Financiadores)
admin.site.register(AreasTecnologicas)


# Register your models here.
