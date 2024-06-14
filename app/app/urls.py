"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from Welcome import views as welcome_views
from Authenticator import views as authenticator_views


router = routers.DefaultRouter()
router.register(r'loans', welcome_views.LoanViewSet)
router.register(r'bills', welcome_views.BillViewSet)
router.register(r'persons', authenticator_views.PersonViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('Authenticator/', include('Authenticator.urls')),
    path('Welcome/', include('Welcome.urls')),
]
