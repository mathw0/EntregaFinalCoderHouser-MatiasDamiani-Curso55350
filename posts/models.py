from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=256)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticia_imagenes', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Info: {self.titulo, self.autor}"
    
class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(max_length=256)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Info: {self.autor, self.noticia, self.fecha}"
