from django.urls import path, include
from user import views
from . import views as edit

urlpatterns = [
    path('', views.base),
    path('login/', views.login),
    path('logout/', views.logout),
    path('taller/', views.taller),
    path('gerencia/', views.gerencia),
    path('secretaria/', views.secretaria),
    path('ventas/', views.ventas),
    path('medico/', views.ProfesionalMedico),
    path('lista/', views.lista) ,
    path('turno/', views.turnoView),
    path('lista/editar/<int:paciente_id>', views.edit),
    path('lista/borrar/<int:paciente_id>', views.borrar),
]