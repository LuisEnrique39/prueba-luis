from django.contrib import admin
from .models import Marca, Producto, tienda, Usuario, Post, Detalle

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(tienda)
admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Detalle)


