"""project_css URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView, DetailView

from ac_citizen.models import CitizenRegister
from app_css import views
from project_css import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html"),name='index'),
    path('active_city/',views.activeCity,name='active_city'),
    path('citi_active/',views.citiActive,name='citi_active'),
    path('admin_active/',views.adminActive,name='admin_active'),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('contact_us/',TemplateView.as_view(template_name='contact_u'
                                                          's.html'),name='contact_us'),


    path('ac_admin/',include('ac_admin.urls')),
    path('ac_login/', include('ac_login.urls')),
    path('ac_officer/', include('ac_officer.urls')),
    path('ac_citizen/', include('ac_citizen.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)