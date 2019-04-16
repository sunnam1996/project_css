from django.shortcuts import render,redirect
from ac_admin.models import Department,Officer
from ac_login.models import LoginUser
from ac_citizen.models import Complaints,Feedback,Reply_feedback
from django.contrib import messages

def admin_add_dept(request):
    qs = Department.objects.all()
    return render(request,"ac_admin/admin_add_dept.html",{"object_list":qs})


def saveDepartment(request):
    if request.method == 'POST':
        dname = request.POST.get("dept_name")
        qs = Department.objects.filter(name=dname)
        if qs:
            qs1 = Department.objects.all()
            return render(request,"ac_admin/admin_add_dept.html",{"msg":"This Dept.Name is Already Available","object_list":qs1})
        else:
            Department(name=dname).save()
            qs = Department.objects.all()
            return render(request,"ac_admin/admin_add_dept.html",{"object_list":qs,"msg":"Department Added"})


def up_Dept(request):
    dname = request.GET.get("name")
    qs = Department.objects.all()
    return render(request,"ac_admin/admin_add_dept.html",{"object_list":qs,"dname":dname})


def delete_Dept(request):
    del_name = request.GET.get("name")
    Department.objects.filter(name=del_name).delete()
    qs = Department.objects.all()
    return render(request,"ac_admin/admin_add_dept.html",{"object_list":qs,"msg":"Department is deleted"})


def update_Dept(request):
    oldname = request.POST.get("old_name")
    newname = request.POST.get("new_name")
    Department.objects.filter(name=oldname).update(name=newname)
    qs = Department.objects.all()
    return render(request,"ac_admin/admin_add_dept.html",{"object_list":qs,"msg":"Department Updated"})


def admin_add_Officer(request):
    qs = Department.objects.all()
    qs1 = Officer.objects.all()
    return render(request,"ac_admin/add_officer.html",{"dept_data":qs,"officer_data":qs1})


def saveOfficer(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    dept = request.POST.get("dept")
    contact = request.POST.get("contact")
    image = request.FILES['image']
    username = request.POST.get("username")
    password = request.POST.get("password")

    message = smsACASMS(contact)
    import json
    d1 = json.loads(message)
    if d1['return']:
        LoginUser(username=username,password=password,type_user="officer").save()
        Officer(idno=idno,name=name,department_id=dept,contact=contact,image=image,username_id=username).save()
        qs = Department.objects.all()
        qs1 = Officer.objects.all()
        return render(request,"ac_admin/add_officer.html",{"dept_data":qs,"officer_data":qs1,"msg":"Officer Added"})
    else:
        qs = Department.objects.all()
        qs1 = Officer.objects.all()
        return render(request, "ac_admin/add_officer.html",
                      {"dept_data": qs, "officer_data": qs1, "msg": "Inavild Contact_No"})


def smsACASMS(contactno):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=hello,Admin Added You&language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "Wq8tZz605vQlRcygT7uF1JO4o3NwrIYHiADndUP2VL9MCKbxsaJftoK3bhwsC5GD7XYvpU2FjquHmicQ",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text


def adminAssigning_complaints(request):
    cid = request.GET.get("cid")
    Complaints.objects.filter(cid=cid).update(status='Assigned')
    return redirect('admin_complaints')


def adminLogout(request):
    del request.session['admin']
    return redirect('admin_index')


def adminFeedbackReply(request):
    fid = request.GET['fid']
    qs = Feedback.objects.filter(fid=fid)
    return render(request,"ac_admin/admin_feedback_reply.html",{"data":qs})


def adminReply_save(request):
    fid = request.POST['fid']
    cid = request.POST['cid']
    ctid = request.POST['ctid']
    message = request.POST['message']
    Reply_feedback(fid_id=fid,cid_id=cid,ct_id_id=ctid,message=message).save()
    messages.error(request,'Reply Sent Successfully')
    return redirect('admin_feedback_reply')