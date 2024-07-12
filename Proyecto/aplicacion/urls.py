from django.urls import path, include
from . import views 

 
urlpatterns =[
path('', views.home, name='inicio'),
path('mujer/', views.mujer, name='mujer'),
path('hombre/', views.hombre,name='hombre'),
path('infantil/', views.infantil, name='infantil'),
path('oversize/', views.oversize,name='oversize'),
path('registro/', views.registro, name='registro'),
path('form',views.registro, name='registro'),
path('lista/',views.crud,name='lista'),
path('del_usuarios/<str:pk>',views.del_usuarios,name='del_usuarios'),
path('mod_usuarios/<str:pk>',views.mod_usuarios,name='mod_usuarios'),
path('insertar_usuario/',views.insertar_usuario,name='insertar_usuario'),

path('login/',views.iniciar_sesion,name="login"),

]