from django.forms import ModelForm
from .models import Paciente


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre','apellido','dni', 'turno', 'historial_medico']
        