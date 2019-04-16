from django.shortcuts import render,redirect
from ac_login.models import LoginUser
from django.contrib import messages
from ac_citizen.models import CitizenRegister
from ac_admin.models import Officer

def loginCheck(request):
    uname = request.POST.get("username")
    upass = request.POST.get("password")
    utype = request.POST.get("utype")
    request.session['admin'] = uname
    qs = LoginUser.objects.filter(username=uname,password=upass,type_user=utype)
    if qs:
        if utype == "admin":
            request.session['admin'] = uname
            return redirect('admin_home')
        elif utype == "citizen":
            qs1 = CitizenRegister.objects.filter(username_id=uname)
            request.session['citizen'] = qs1[0].name
            request.session['ctid'] = qs1[0].ct_id
            if qs1[0].status == "Active":
                print(qs1[0].name)
                return redirect('citizen_home')
            else:
                return render(request,"ac_citizen/citizen_index.html",{"mssg":"Otp Verification Not Complete"})
        else:
            qs2 = Officer.objects.filter(username_id=uname)
            request.session['officer'] = qs2[0].name
            request.session['dept'] = qs2[0].department_id
            return redirect('officer_home')
    else:
        if utype == 'admin':
            messages.error(request,"Invalid Admin Details")
            return redirect('admin_index')
        elif utype == 'officer':
            messages.error(request,"Invalid Officer Details")
            return redirect('officer_index')
        else:
            messages.error(request,"Invalid Citizen Details")
            return redirect('citizen_index')
