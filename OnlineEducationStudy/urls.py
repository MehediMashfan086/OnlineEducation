from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from edu import views as edu_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edu.urls')),
    path('register/', edu_views.register, name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name = 
    "edu/login.html"), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 
    "edu/logout.html"), name = 'logout'),
    path('profile/', edu_views.profile, name = 'profile'),
]
