from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleados
from .forms import EmpleadosForm

def lista_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, './lista_empleados.html',{'empleados': empleados})

def crear_empleado(request):
    show_success_message = False

    if request.method == 'POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save() # Guarda los datos en la Base de Datos
            show_success_message = True
    else:
        form = EmpleadosForm()

    return render(request, 'crear_empleado.html', {'form' : form, 'show_success_message': show_success_message})

def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleados, id=empleado_id)

    if request.method == 'POST':
        form = EmpleadosForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
        form = EmpleadosForm(instance=empleado)

    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)
    empleado.delete()
    return redirect('empleados')