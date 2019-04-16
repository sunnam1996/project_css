from django.shortcuts import render,redirect
from ac_citizen.models import Complaints,Feedback
import datetime


def officerClosing_complaints(request):
    dt = datetime.date.today()
    cid = request.GET['cid']
    Complaints.objects.filter(cid=cid).update(status='Closed',close_date=dt)
    return redirect('officer_complaints')


def officerLogout(request):
    del request.session['officer']
    return redirect('officer_index')


def officerFeedback(request):
    qs = Complaints.objects.all()
    qs1 = Feedback.objects.all()
    return render(request,"ac_officer/officer_feedback.html",{"C_data":qs,"F_data":qs1})