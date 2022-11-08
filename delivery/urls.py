from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('login/', auth.LoginView.as_view(template_name='sign_in.html')),
    path('logout/', auth.LogoutView.as_view(next_page='/')),

    path('customer/', views.customer_page, name='customer'),
    path('courier/', views.courier_page, name='courier'),
]
