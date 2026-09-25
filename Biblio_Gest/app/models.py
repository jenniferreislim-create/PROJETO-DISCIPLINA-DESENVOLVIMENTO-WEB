from django.db import models

# Create your models here.
class Usuário(models.Model):
    nome = models.CharField(max_length=100)
    vinculo = models.CharField(max_length=10)

    def __str__(self):
        return self.nome + ' - ' + self.vinculo


class Empréstimo(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)

    livros= models.CharField(max_length=50)
    dataEmprestimo = models.DateField()
    dataDevolucao = models.DateField()

    def __str__(self):
        return self.livros + ' - ' + self.dataEmprestimo + ' - ' + self.dataDevolucao

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + ' - ' + self.autor