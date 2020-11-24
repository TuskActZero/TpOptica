from django.forms import ModelForm
from .models import Paciente, Turno
from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.contrib.admin import widgets

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre','apellido','dni', 'turno', 'historial_medico', ]


class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets={
            'fecha':forms.DateInput(attrs
            ={'type':'datetime-local'},
            format='%Y%m%dT%H:%M'),
        }