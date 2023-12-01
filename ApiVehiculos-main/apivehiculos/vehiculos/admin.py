from django.contrib import admin

from .models import Vehiculo
from .models import VehiculoDocumento

admin.site.register(Vehiculo)
admin.site.register(VehiculoDocumento)
