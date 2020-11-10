from django.urls import path
from . import views
app_name = 'login'
urlpatterns = [
    path('', views.index, name='root'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    path('logout', views.logout, name='logout')
]