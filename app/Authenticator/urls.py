from django.urls import path
from django.conf.urls import include
from . import views
import Welcome.views as welcome_views


app_name = "Authenticator"

urlpatterns = [
    path('api', views.PersonViewSet.as_view({'get':'list'})),
    path('api/register-user', views.index, name="index"),
    path('Authenticator/login.html', views.login, name="login"),
    path('Welcome/index.html', welcome_views.index)
]
