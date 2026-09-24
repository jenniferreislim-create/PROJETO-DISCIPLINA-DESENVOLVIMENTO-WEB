from django.shortcuts import render, redirect, get_object_or_404
from.models import Empréstimo, Usuário, Livro
from .forms import UsuarioForm, LivroForm


def home(request):
    return render(request, 'home.html')

def emprestimo_form(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        vinculo = request.POST['vinculo']
        livros = request.POST['livros']
        dataEmprestimo = request.POST['dataEmprestimo']
        dataDevolucao = request.POST['dataDevolucao']


        p = Empréstimo.objects.create(nome=nome, livros=livros,
                dataEmprestimo=dataEmprestimo, dataDevolucao=dataDevolucao)


        print(p.id)

        return redirect('app:emprestimo_list')

    return render(request, 'emprestimo_form.html')

def emprestimo_list(request):
    emprestimos = Empréstimo.objects.all()
    #get_objects(Emprestimo)
    return render(request, 'emprestimo_list.html',
                  {'emprestimos': emprestimos})

def emprestimo_edit(request, pk):
    if pk:
        emprestimo = Empréstimo.objects.get(pk=pk)
    else:
        emprestimo = None

    if request.method == 'POST':
        nome = request.POST['nome']
        vinculo = request.POST['vinculo']
        livros = request.POST['livros']
        dataEmprestimo = request.POST['dataEmprestimo']
        dataDevolucao = request.POST['dataDevolucao']

        return redirect('app:emprestimo_list')
    return render(request, 'emprestimo_form.html', {'emprestimo': emprestimo})

def emprestimo_delete(request, pk):
    if pk:
        emprestimo = Empréstimo.objects.get(pk=pk)
        emprestimo.delete()
        return redirect('app: emprestimo_list')


def usuario_form(request):
    form = UsuarioForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('app:usuario_list')
    return render(request, 'usuario_form.html', {'form': form})

def usuario_list(request):
    usuarios = Usuário.objects.all()
    return render(request, 'usuario_list.html',
                  {'usuarios': usuarios})

def usuario_edit(request, pk):
    usuario = None
    if pk:
        usuario = get_object_or_404(Usuário, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('app:usuario_list')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    if pk:
        usuario = get_object_or_404(Usuário, pk=pk)
        usuario.delete()
        return redirect('app:usuario_list')
    return render(request, 'usuario_form.html')




def livro_form(request):
    form = LivroForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('app:livro_list')
    return render(request, 'livro_form.html', {'form': form})

def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'livro_list.html',
                  {'livros': livros})

def livro_edit(request, pk):
    livro = None
    if pk:
        livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('app:livro_list')
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livro_form.html', {'form': form})

def livro_delete(request, pk):
    if pk:
        livro = get_object_or_404(Livro, pk=pk)
        livro.delete()
        return redirect('app:livro_list')
    return render(request, 'livro_form.html')