from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index), 
    path('cita/', views.cita),
    path('quote/', views.quote),
    path('administrador/', views.administrador),
    path('user/<int:id>', views.user),
    path('editar/<int:id>', views.editar),
    path('borrar/<int:id>', views.borrar),

    #URL DE REGISTROS
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout)

]
