from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.base),
    path('login/', views.login),
    path('logout/', views.logout),
    path('taller/', views.taller),
    path('gerencia/', views.gerencia),
    path('secretaria/', views.secretaria),
    path('ventas/', views.ventas),
    path('medico/', views.ProfesionalMedico),
]