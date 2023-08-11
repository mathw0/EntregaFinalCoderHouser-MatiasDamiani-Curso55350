from django.contrib import admin
from django.urls import path, include
from Proyecto_final.views import inicio, acerca, statics
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('acerca', acerca),
    path('statics', statics),
    path('blog/', include("blog.urls")),
    path('perfiles/', include("perfiles.urls")),
    path('posts/', include("posts.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)