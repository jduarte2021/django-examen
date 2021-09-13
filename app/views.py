from app.models import User, Quote
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
import bcrypt
from .decorators import login_required,admin_requerido


@login_required
def index(request):

    context = {

    }
    return redirect('/cita')

def cita(request):
    if 'usuario' not in request.session:
        messages.error(request, "No estas logeado")
        return redirect("/login")
    
    context = {
        'quotes' : Quote.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    }
    return render(request, 'index.html', context)

@admin_requerido
def administrador(request):

    context = {
        'saludo': 'ADMINISTRADOR'
    }
    return render(request, 'admin.html', context)

def quote(request):
    if request.method == "POST":
        errors = User.objects.validador_citas(request.POST)
        # print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            request.session['register_autor'] =  request.POST['autor']
            request.session['register_mensaje'] =  request.POST['mensaje']

        else:
            request.session['register_autor'] =  ""
            request.session['register_mensaje'] = ""
            mensaje = request.POST['mensaje']
            usuarios = request.session['usuario']
            mensajebd = Quote.objects.create(
                usuario_id = usuarios['id'],
                autor = request.POST['autor'],
                mensaje = request.POST['mensaje'],
            )
    return redirect("/cita")

def user(request,id):
    context = {
        'usuario': User.objects.filter(id=id),
        'citas' : Quote.objects.filter(usuario_id=id)
    }
    return render(request, 'user.html', context)

def editar(request,id):
    print(request.POST)
    if request.method == 'POST':
        usuario = User.objects.get(id=id)
        usuario.name = request.POST['name']
        usuario.lastname = request.POST['lastname']
        usuario.email = request.POST['email']
        usuario.save()
        messages.success(request,"Edicion satisfactoria")
        return redirect(f"/editar/{id}")
    else:
        
        context = {
                'datos' : User.objects.get(id=id),
        }

        return render(request, 'editar.html', context)


def borrar(request,id):
    print(request.POST)
    borrar = Quote.objects.filter(id=id).delete()
    messages.error(request, "Cita eliminada")

    return redirect("/")