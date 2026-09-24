from django.urls import path
from .views import home, emprestimo_form,emprestimo_list, emprestimo_edit, emprestimo_delete
from .views import usuario_form, usuario_list, usuario_edit, usuario_delete
from .views import livro_form, livro_list, livro_edit, livro_delete

app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('emprestimo/list/', emprestimo_list, name= 'emprestimo_list'),
    path('emprestimo/cadastrar/', emprestimo_form, name= 'emprestimo_form'),
    path('emprestimo/editar/<int:pk>', emprestimo_edit, name='emprestimo_edit'),
    path('emprestimo/deletar/<int:pk>', emprestimo_delete, name='emprestimo_delete'),
    path('usuario/cadastrar/', usuario_form, name='usuario_form'),
    path('usuario/list', usuario_list, name='usuario_list'),
    path('usuario/editar/<int:pk>', usuario_edit, name='usuario_edit'),
    path('usuario/deletar/<int:pk>', usuario_delete, name='usuario_delete'),
    path('livro/list/', livro_list, name='livro_list'),
    path('livro/cadastrar/', livro_form, name='livro_form'),
    path('livro/editar/<int:pk>', livro_edit, name='livro_edit'),
    path('livro/deletar/<int:pk>', livro_delete, name='livro_delete'),


]