from django.shortcuts import render
from .models import clientes

# Create your views here.

def status(req): 
    return render(req, 'status.html', {
        "titulo": 'Status',
        "clientes": list(clientes.objects.values())
    })