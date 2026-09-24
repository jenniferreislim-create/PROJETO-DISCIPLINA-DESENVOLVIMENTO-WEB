from django import forms
from .models import Usuário, Empréstimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Empréstimo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'vinculo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Vinculo'}),
            'livro': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Livro'}),
            'dataEmprestimo': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de Emprestimo'}),
            'dataDevolucao': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de Devolução'}),

        }

        labels = {
            'nome': 'Nome',
            'vinculo': 'Vinculo',
            'livro': 'Livro',
            'dataEmprestimo': 'Data de Emprestimo',
            'dataDevolucao' : 'Data de Devolucao',
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuário
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'vinculo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Vinculo'}),
        }

        labels = {
            'nome': 'Nome',
            'vinculo': 'Vinculo',
        }