from django.shortcuts import render,redirect
from django.contrib import messages
from ac_admin.models import Department
from ac_citizen.models import CitizenRegister, Complaints,Feedback,Reply_feedback
from ac_login.models import LoginUser


def citizen_Save(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact_no = request.POST.get("contact")
        city = request.POST.get("city")
        address = request.POST.get("address")
        image = request.FILES['image']
        uname = request.POST.get("username")
        upass = request.POST.get("password")

        one = name[0]
        two = contact_no[-5]
        three = uname[-2]
        four = upass[3]
        five = address[2]

        otp = four + one + str(two) + three + five

        message = smsACASMSotp(contact_no,otp)
        import json
        d1 = json.loads(message)
        if d1['return']:
            LoginUser(username=uname, password=upass, type_user="citizen").save()
            CitizenRegister(name=name,contact=contact_no,city=city,address=address,image=image,username_id=uname,otp=otp,status="pending").save()
            qs = CitizenRegister.objects.all()
            qs1 = CitizenRegister.objects.filter(contact=contact_no,otp=otp)
            return render(request, "ac_citizen/citizen_verification.html",
                          {"citizen_data": qs,"citi_data":qs1})
        else:
            return render(request, "ac_citizen/citizen_register.html",
                          {"msg": "Inavild Contact_No"})

def smsACASMSotp(contactno,otp):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello,Your OneTimePassword of Registration is "+ otp +"&language=english&route=p&numbers=" + contactno
    headers = {
        'authorization': "Wq8tZz605vQlRcygT7uF1JO4o3NwrIYHiADndUP2VL9MCKbxsaJftoK3bhwsC5GD7XYvpU2FjquHmicQ",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text


def citizen_Verification(request):
    if request.method == "POST":
        contact_no = request.POST.get("cno")
        otp = request.POST.get("otp")
        qs = CitizenRegister.objects.filter(contact=contact_no,otp=otp)
        if qs:
            CitizenRegister.objects.filter(contact=contact_no).update(status="Active")
            return render(request,"ac_citizen/citizen_index.html",{"msg":"Registered successfully"})
        else:
            return render(request,"ac_citizen/citizen_verification.html",{"msg":"Wrong Otp"})


def citizenComplaintSave(request):
    if request.method == "POST":
        cid = request.POST.get('cid')
        ctid = request.POST.get('ctid')
        dname = request.POST.get('dept')
        message = request.POST.get('message')
        image = request.FILES['image']
        Complaints(cid=cid,ct_id_id=ctid,department_id=dname,message=message,image=image,status='pending').save()
        qs = Department.objects.all()
        return render(request,"ac_citizen/citizen_complaint_register.html",{"object_list":qs,"msg":"Complaint Successfully Registered"})

def citizenProf(request):
    qs = CitizenRegister.objects.all()
    return render(request,"ac_citizen/citizen_profile.html",{"object":qs})


def citizenLogout(request):
    del request.session['ctid']
    del request.session['citizen']
    return redirect('citizen_index')


def citizenFeedback_Saved(request):
    if request.method == 'POST':
        cid = request.POST['cid']
        ctid = request.POST['ctid']
        message = request.POST['message']
        image = request.FILES['image']
        Feedback(cid_id=cid,ct_id_id=ctid,message=message,image=image).save()
        messages.error(request,'Feedback Successfully Sent')
        return redirect('complaints_feedback')


def complintsFeedback(request):
    qs = Complaints.objects.all()
    qs1 = Feedback.objects.all()
    return render(request,"ac_citizen/complaints_feedback.html",{"object_list":qs,"feeddata":qs1})


def citizenReply_check(request):
    fid = request.GET['fid']
    cid = request.GET['cid']
    ctid = request.GET['ctid']
    qs = Reply_feedback.objects.filter(fid_id=fid,cid_id=cid,ct_id_id=ctid)
    return render(request,"ac_citizen/citizen_reply_check.html",{"object_list":qs})
