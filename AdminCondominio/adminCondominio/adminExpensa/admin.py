from django.contrib import admin
from .models import Propietario
from .models import Departamento
from .models import Expensa_Agua
from .models import Expensa



admin.site.register(Propietario)
admin.site.register(Departamento)
admin.site.register(Expensa_Agua)
admin.site.register(Expensa)

