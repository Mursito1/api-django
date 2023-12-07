from django.contrib import admin
from .models import Profesor
from .models import Alumno

# Register your models here.

admin.site.register(Profesor)
admin.site.register(Alumno)
