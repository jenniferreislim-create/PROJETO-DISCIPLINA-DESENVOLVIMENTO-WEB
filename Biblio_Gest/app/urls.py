from django.urls import path
from .views import home, emprestimo_form,emprestimo_list


app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('emprestimo/list/', emprestimo_list, name= 'emprestimo_list'),
    path('emprestimo/cadastrar/', emprestimo_form, name= 'emprestimo_form'),
]