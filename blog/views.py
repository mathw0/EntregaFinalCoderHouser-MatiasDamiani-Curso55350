from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import contactus
from django.contrib.auth.decorators import login_required
from posts.models import Noticia, Comentario

def inicio_blog(request):
    HttpResponse = render(request=request, template_name='blog/inicio_blog.html', context={})
    return HttpResponse

def statics(request):
    HttpResponse = render(request=request, template_name='blog/statics.html', context={})
    return HttpResponse

def prueba(request):
    HttpResponse = render(request=request, template_name='blog/prueba.html', context={})
    return HttpResponse

@login_required(login_url='login_error')  # 'login' es el nombre de la URL para el formulario de inicio de sesión
def posts(request):
    HttpResponse = render(request=request, template_name='blog/posts.html', context={})
    return HttpResponse


def Contactarnos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        consulta = request.POST.get('consulta') 

        if nombre and apellido and consulta and email:
            consultas_generales = contactus(nombre=nombre, apellido=apellido, consulta=consulta, email=email, telefono=telefono)
            consultas_generales.save()
            return redirect('/blog/inicio_blog')
        error_message = "Todos los campos son obligatorios."
        return render(request=request, template_name='blog/contactus.html', context={'error_message': error_message})
    
    return render(request=request, template_name='blog/contactus.html')

def inicio_blog(request):
    ultimos_comentarios = Comentario.objects.all().order_by('-fecha')[:5]

    return render(request, 'blog/inicio_blog.html', {'ultimos_comentarios': ultimos_comentarios})

def buscar_noticias(request):
    if 'q' in request.GET:
        query = request.GET['q']
        noticias = Noticia.objects.filter(titulo__icontains=query)
    else:
        noticias = Noticia.objects.none()  # Sin resultados si no se proporciona una búsqueda
    
    return render(request, 'blog/resultados_busqueda.html', {'noticias': noticias, 'query': query})