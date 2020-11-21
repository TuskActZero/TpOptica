from django.forms import ModelForm
from .models import Paciente, Turno
from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre','apellido','dni', 'turno', 'historial_medico', ]

class TurnoForm(ModelForm):
    class Meta:
        model=Turno
        fields=['hora_turno']
        hora_turno = forms.DateField(widget=DatePicker())
