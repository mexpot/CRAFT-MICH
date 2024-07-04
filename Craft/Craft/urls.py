"""
URL configuration for Craft project.

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
from michoacan import views
from django.conf import settings
from base import views as views_base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ca/', views.ca, name="ca"),
    path('', views_base.Carrusel, name="Carrusel"),
    path('ForCarrusel/',views_base.contacto,name="Contacto"),
    path('registrar/',views_base.registrar,name="Registrar"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)