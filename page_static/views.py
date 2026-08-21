from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def contatos(request):
    return render(request,'contatos.html')

def servicos(request):
    return render(request,'servicos.html')

def sobre(request):
    return render(request,'sobre.html')