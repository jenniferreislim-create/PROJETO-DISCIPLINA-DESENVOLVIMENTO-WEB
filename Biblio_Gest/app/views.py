from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def emprestimo_form(request):
    return render(request, 'emprestimo_form.html')

def emprestimo_list(request):
    return render(request, 'emprestimo_list.html')