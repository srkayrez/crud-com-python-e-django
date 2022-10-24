from django.shortcuts import render, redirect
from crud.forms import ContatosForm
from crud.forms import Contatos

# Create your views here.
def home(request):
    data = {}
    data['db'] = Contatos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ContatosForm()
    return render(request, 'form.html', data)

def create(request):
    form = ContatosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Contatos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Contatos.objects.get(pk=pk)
    data['form'] = ContatosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Contatos.objects.get(pk=pk)
    form = ContatosForm(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request,pk):
    db = Contatos.objects.get(pk=pk)
    db.delete()
    return redirect('home')