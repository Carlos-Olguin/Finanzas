from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Categoria, Transaccion, Presupuesto

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Categoria)
admin.site.register(Transaccion)
admin.site.register(Presupuesto)
