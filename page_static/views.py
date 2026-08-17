from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Essa é view de teste</h1>")

def contatos(request):
    return HttpResponse("<p>telefone:(21)96546-64564</p><p>Email:seo@gmail.com</p>")