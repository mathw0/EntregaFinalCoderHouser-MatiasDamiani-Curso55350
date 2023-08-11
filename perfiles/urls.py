from django.contrib import admin
from django.urls import path, include
from blog.views import inicio_blog
from django.conf import settings
from django.conf.urls.static import static


from perfiles.views import (
    registro, login_view, CustomLogoutView, MiPerfilUpdateView, agregar_avatar, login_error,
)


urlpatterns = [
    # URLS Usuario y sesion
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('editar_datos/', MiPerfilUpdateView.as_view(), name="editar_datos"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
    path('inicio_blog/', inicio_blog, name='inicio_blog'),
    path('login-error/', login_error, name='login_error'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)