from django.contrib import admin
from .models import Paciente, Turno, Pedido, Lente

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    model = Paciente
    list_display=("nombre", "apellido", "dni", "turno", "historial_medico")
    list_filter=("turno",)
 

class TurnoAdmin(admin.ModelAdmin):

    model = Turno

    
class PedidoAdmin(admin.ModelAdmin):
    model = Pedido

class LenteAdmin(admin.ModelAdmin):
    model = Lente
    list_display= ("nombre_lente", "precio")





admin.site.register(Paciente ,PacienteAdmin)
admin.site.register(Turno ,TurnoAdmin)
admin.site.register(Pedido ,PedidoAdmin)
admin.site.register(Lente ,LenteAdmin)

