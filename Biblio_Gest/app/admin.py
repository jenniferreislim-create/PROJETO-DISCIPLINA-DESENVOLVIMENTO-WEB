from django.contrib import admin

# Register your models here.
from .models import Usuário, Empréstimo, Livro
from django.contrib import admin

admin.site.register(Usuário)
admin.site.register(Empréstimo)
admin.site.register(Livro)
