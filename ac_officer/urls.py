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
from django.urls import path
from django.views.generic import TemplateView, ListView
from ac_admin.models import Officer
from ac_citizen.models import Complaints
from ac_officer import views
from project_css import settings

urlpatterns = [
    path('officer_index/', TemplateView.as_view(template_name="ac_officer/officer_index.html"), name='officer_index'),
    path('officer_home/',TemplateView.as_view(template_name="ac_officer/officer_home.html"),name='officer_home'),
    path('officer_complaints/',TemplateView.as_view(template_name="ac_officer/officer_complaints.html"),name='officer_complaints'),
    path('officer_assigned_complaints/',ListView.as_view(template_name="ac_officer/officer_assigned_complaints.html", model=Complaints,queryset=Complaints.objects.filter(status='Assigned')), name='officer_assigned_complaints'),
    path('officer_closing_complaints/',views.officerClosing_complaints,name='officer_closing_complaints'),
    path('officer_closed_complaints/',ListView.as_view(template_name="ac_officer/officer_closed_complaints.html", model=Complaints,queryset=Complaints.objects.filter(status='Closed')), name='officer_closed_complaints'),
    path('officer_prof/',ListView.as_view(template_name='ac_officer/officer_prof.html',model=Officer),name='officer_prof'),
    path('officer_feedback/',views.officerFeedback,name='officer_feedback'),



    path('officer_logout/',views.officerLogout,name='officer_logout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)