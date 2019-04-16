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
from django.views.generic import TemplateView, ListView, DetailView

from ac_admin.models import Department
from ac_citizen import views
from ac_citizen.models import Complaints,CitizenRegister
from project_css import settings

urlpatterns = [
    path('citizen_index/', TemplateView.as_view(template_name="ac_citizen/citizen_index.html"), name='citizen_index'),
    path('citizen_home/',TemplateView.as_view(template_name="ac_citizen/citizen_home.html"),name='citizen_home'),
    path('citizen_register/',TemplateView.as_view(template_name="ac_citizen/citizen_register.html"),name='citizen_register'),
    path('citizen_registration_save/',views.citizen_Save,name='citizen_registration_save'),
    path('citizen_verification/',views.citizen_Verification, name='citizen_verification'),
    path('citizen_otp_check/', TemplateView.as_view(template_name='ac_citizen/citizen_otp_validate.html'),name='citizen_otp_check'),
    path('citizen_complaint_register/',ListView.as_view(template_name="ac_citizen/citizen_complaint_register.html", model=Department),name='citizen_complaint_register'),
    path('citizen_complaint_save/', views.citizenComplaintSave, name='citizen_complaint_save'),
    path('citizen_complaint_status/', TemplateView.as_view(template_name="ac_citizen/citizen_complaint_status.html"),name='citizen_complaint_status'),
    path('citizen_pending_complaints/',ListView.as_view(template_name="ac_citizen/citizen_pending_complaints.html", model=Complaints,queryset=Complaints.objects.filter(status='pending')), name='citizen_pending_complaints'),
    path('citizen_assigned_complaints/',ListView.as_view(template_name="ac_citizen/citizen_assigned_complaints.html", model=Complaints,queryset=Complaints.objects.filter(status='Assigned')), name='citizen_assigned_complaints'),
    path('citizen_closed_complaints/',ListView.as_view(template_name="ac_citizen/citizen_closed_complaints.html", model=Complaints,queryset=Complaints.objects.filter(status='Closed')), name='citizen_closed_complaints'),
    path('complaints_feedback/',views.complintsFeedback,name='complaints_feedback'),
    path('citizen_feedback_saved/',views.citizenFeedback_Saved,name='citizen_feedback_saved'),
    path('reply_check/',views.citizenReply_check,name='reply_check'),

    path('citizen_prof/',views.citizenProf,name='citizen_prof'),
    path('citizen_logout/',views.citizenLogout,name='citizen_logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)