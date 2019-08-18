from django.urls import path
from .views import UserRegisterView
from blog.views import post_list_view
from django.contrib.auth import views as views_auth


urlpatterns = [
    path('register/', UserRegisterView, name="register"),
    path('login/', views_auth.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', views_auth.LogoutView.as_view (template_name = 'users/logout.html'), name='logout'),
    path('', post_list_view, name="home"),
]
