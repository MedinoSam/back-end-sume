
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('projetos/listar', views.get_projetos, name = 'get_todos_projetos'),
    path('projetos/cadastrar', views.post_projetos, name = 'cadastra_projeto'),
    path('projetos/<int:pk>/inativar', views.inativar_por_id, name = 'inativar_projeto_por_id'),
    path('projetos/<int:pk>/editar', views.editar_projeto, name = 'editar_projeto'),
    path('projetos/<int:pk>/visualizar', views.get_projetos_id, name = 'get_projeto_por_id'),
    path('projetos/<int:pk>/equipe', views.get_equipe_id, name = 'get_equipe_por_id'),
    path('projetos/<int:pk>/equipe/atualizar', views.editar_equipe_projeto, name = 'editar_equipe_projeto'),
    path('colaboradores/listar', views.get_todos_colaboradores, name = 'get_todos_colaboradores'),
    path('colaboradores/cadastrar', views.cadastra_colaborador, name = 'cadastra_colaborador'),
    path('colaboradores/<int:pk>/visualizar', views.get_colaborador_by_id, name = 'get_colaborador_por_id'),
    path('colaboradores/<int:pk>/editar', views.editar_colaborador_by_id, name = 'editar_colaborador_por_id')

]
