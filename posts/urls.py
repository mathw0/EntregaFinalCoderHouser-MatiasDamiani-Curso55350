from django.contrib import admin
from django.urls import path
from posts.views import (crear_noticia, mostrar_noticia, mostrar_noticias, editar_noticia, borrar_noticia, agregar_comentario, ultimos_comentarios, mis_noticias)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('crear_noticia/', crear_noticia, name='crear_noticia'),
    path('noticias/', mostrar_noticias, name='mostrar_noticias'),
    path('editar_noticia/<int:noticia_id>/', editar_noticia, name='editar_noticia'),
    path('borrar_noticia/<int:noticia_id>/', borrar_noticia, name='borrar_noticia'),
    path('agregar_comentario/<int:noticia_id>/', agregar_comentario, name='agregar_comentario'),
    path('noticia/<int:noticia_id>/', mostrar_noticia, name='mostrar_noticia'),
    path('ultimos_comentarios/', ultimos_comentarios, name='ultimos_comentarios'),
    path('mis_noticias/', mis_noticias, name='mis_noticias'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)