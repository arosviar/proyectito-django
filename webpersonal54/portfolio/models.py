from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Articulo")
    description = models.TextField(verbose_name= "Descripcion")
    #image = models.ImageField(verbose_name= "Imagen", upload_to= 'projects')
    link = models.PositiveBigIntegerField (verbose_name= "Precio $", null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de Modificación")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= "proyecto"
        verbose_name_plural= "proyectos"
        ordering = ["-created"]