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

from ac_admin import views
from ac_citizen.models import Complaints,Feedback
from project_css import settings

urlpatterns = [
    path('admin_index/',TemplateView.as_view(template_name="ac_admin/admin_index.html"),name='admin_index'),
    path('admin_home/', TemplateView.as_view(template_name="ac_admin/admin_home.html"), name='admin_home'),
    path('admin_add_dept/',views.admin_add_dept,name='admin_add_dept'),
    path('save_department/',views.saveDepartment,name='save_department'),
    path('up_dept/',views.up_Dept,name='up_dept'),
    path('del_dept/',views.delete_Dept,name='del_dept'),
    path('update_dept/',views.update_Dept,name='update_dept'),
    path('add_officer/',views.admin_add_Officer,name='add_officer'),
    path('save_officer/',views.saveOfficer,name='save_officer'),
    path('admin_complaints/',TemplateView.as_view(template_name="ac_admin/admin_complaints.html"),name='admin_complaints'),
    path('admin_pending_complaints/',ListView.as_view(template_name="ac_admin/admin_pending_complaints.html", model=Complaints,queryset=Complaints.objects.filter(status='pending')), name='admin_pending_complaints'),
    path('admin_assigning_complaints/',views.adminAssigning_complaints,name='admin_assigning_complaints'),
    path('admin_assigned_complaints/',ListView.as_view(template_name="ac_admin/admin_assigned_complaints.html", model=Complaints,queryset=Complaints.objects.filter(status='Assigned')), name='admin_assigned_complaints'),
    path('admin_closed_complaints/',ListView.as_view(template_name="ac_admin/admin_closed_complaints.html", model=Complaints,queryset=Complaints.objects.filter(status='Closed')), name='admin_closed_complaints'),
    path('admin_feedback/',ListView.as_view(template_name='ac_admin/admin_feedback.html',model=Feedback),name='admin_feedback'),
    path('admin_feedback_reply/',views.adminFeedbackReply,name='admin_feedback_reply'),
    path('admin_reply_save/',views.adminReply_save,name='admin_reply_save'),
    path('admin_logout/',views.adminLogout,name='admin_logout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)