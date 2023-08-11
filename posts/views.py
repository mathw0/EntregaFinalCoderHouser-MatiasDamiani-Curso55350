from django.shortcuts import render, redirect, get_object_or_404
from posts.forms import NoticiaForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from posts.models import Noticia, Comentario

@login_required(login_url='login_error')
def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_noticia = form.save(commit=False)
            nueva_noticia.autor = request.user
            nueva_noticia.save()
            return redirect('mostrar_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'posts/crear_noticia.html', {'form': form})


def mostrar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'posts/noticias.html', {'noticias': noticias})

@login_required(login_url='login_error')
def editar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id, autor=request.user)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('mostrar_noticias')
    else:
        form = NoticiaForm(instance=noticia)
    
    return render(request, 'posts/editar_noticia.html', {'form': form, 'noticia': noticia})

@login_required(login_url='login_error')
def borrar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    if request.method == 'POST':
        noticia.delete()
        return redirect('mostrar_noticias')

    return render(request, 'posts/borrar_noticia.html', {'noticia': noticia})

@login_required(login_url='login_error')
def agregar_comentario(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.autor = request.user
            nuevo_comentario.noticia = noticia
            nuevo_comentario.save()
            return redirect('mostrar_noticia', noticia_id=noticia_id)

    else:
        form = ComentarioForm()

    return render(request, 'posts/agregar_comentario.html', {'form': form, 'noticia': noticia})

@login_required(login_url='login_error')
def mostrar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    
    comentario_form = ComentarioForm()  # Crear una instancia del formulario de comentarios
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.autor = request.user
            nuevo_comentario.noticia = noticia
            nuevo_comentario.save()
            return redirect('mostrar_noticia', noticia_id=noticia_id)
    
    return render(request, 'posts/mostrar_noticia.html', {'noticia': noticia, 'comentario_form': comentario_form})

def ultimos_comentarios(request):
    comentarios = Comentario.objects.order_by('-fecha')[:5]
    return render(request, 'posts/ultimos_comentarios.html', {'comentarios': comentarios})

@login_required(login_url='login_error')
def mis_noticias(request):
    user = request.user
    noticias = Noticia.objects.filter(autor=user)
    return render(request, 'posts/mis_noticias.html', {'noticias': noticias})