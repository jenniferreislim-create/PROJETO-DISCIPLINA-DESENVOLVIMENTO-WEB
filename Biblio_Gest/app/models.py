from django.db import models

# Create your models here.
class Usuário(models.Model):
    nome = models.CharField(max_length=100)
    vinculo = models.CharField(max_length=10)


class Empréstimo(models.Model):
    livros= models.CharField(max_length=50)
    dataEmprestimo = models.DateField()
    dataDevolução = models.DateField()

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)