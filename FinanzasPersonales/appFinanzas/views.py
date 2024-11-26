from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Transaccion, CustomUser
from .forms import TransaccionForm

def lista_transacciones(request):
    # Obtener todas las transacciones
    transacciones = Transaccion.objects.all().order_by('-fecha')
    context = {
        'transacciones': transacciones,
        'total_ingresos': sum(t.monto for t in transacciones if t.tipo == 'Ingreso'),
        'total_gastos': sum(t.monto for t in transacciones if t.tipo == 'Gasto'),
    }
    return render(request, 'appFinanzas/transacciones_lista.html', context)

def crear_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            transaccion = form.save(commit=False)
            # Asignar el primer usuario por ahora
            transaccion.usuario = CustomUser.objects.first()
            transaccion.save()
            messages.success(request, 'Transacción creada exitosamente.')
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm()
    
    return render(request, 'appFinanzas/transaccion_form.html', {
        'form': form,
        'accion': 'Crear'
    })

def editar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == 'POST':
        form = TransaccionForm(request.POST, instance=transaccion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transacción actualizada exitosamente.')
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm(instance=transaccion)
    
    return render(request, 'appFinanzas/transaccion_form.html', {
        'form': form,
        'accion': 'Editar'
    })

def eliminar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == 'POST':
        transaccion.delete()
        messages.success(request, 'Transacción eliminada exitosamente.')
        return redirect('lista_transacciones')
    return render(request, 'appFinanzas/transaccion_confirmar_eliminar.html', {
        'transaccion': transaccion
    })
