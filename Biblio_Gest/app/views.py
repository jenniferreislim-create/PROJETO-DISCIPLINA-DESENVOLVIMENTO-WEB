from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def empréstimo_form(request):
    return render(request, 'empréstimo_form.html')

def empréstimo_list(request):
    return render(request, 'empréstimo_list.html')