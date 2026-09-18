from django.urls import path
from .views import home, empréstimo_form,empréstimo_list


app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('empréstimo/', empréstimo_list, name= 'empréstimo_list'),
    path('empréstimo/cadastrar/', empréstimo_form, name= 'empréstimo_form'),
]