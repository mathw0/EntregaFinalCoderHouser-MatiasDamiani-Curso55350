from django.urls import path
from blog.views import (inicio_blog, statics, prueba, Contactarnos, posts, buscar_noticias)
from posts.views import ultimos_comentarios
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('inicio_blog/', inicio_blog, name="inicio_blog"),
    path('statics', statics),
    path('prueba', prueba),
    path('contact', Contactarnos),
    path('posts', posts),
    path('ultimos_comentarios/', ultimos_comentarios, name="ultimos_comentarios"),
    path('buscar_noticias/', buscar_noticias, name='buscar_noticias'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)