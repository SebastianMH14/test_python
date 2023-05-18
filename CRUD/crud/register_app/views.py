from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Registro
from .forms import RegistroForm

def registro_list(request):
    registros = Registro.objects.all()
    return render(request, 'registro_list.html', {'registros': registros})

def registro_create(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro-list')
    else:
        form = RegistroForm()
    return render(request, 'registro_create.html', {'form': form})

def registro_update(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('registro-list')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'registro_update.html', {'form': form, 'registro': registro})

def registro_delete(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('registro-list')
    return render(request, 'registro_delete.html', {'registro': registro})
