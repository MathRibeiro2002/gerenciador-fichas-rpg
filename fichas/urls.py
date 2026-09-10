from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar/', views.criar_ficha, name='criar_ficha'),
    path('ficha/<int:id>/', views.detalhes_ficha, name='detalhes_ficha'),
    path('ficha/<int:id>/editar/', views.editar_ficha, name='editar_ficha'),
    path('ficha/<int:id>/deletar/', views.deletar_ficha, name='deletar_ficha'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='fichas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]