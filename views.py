import datetime
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage

# Create your views here.
from FitWell.models import*


def login(request):
    return render(request, 'index.html')

def login_post(request):
    usn = request.POST['textfield']
    psd = request.POST['textfield2']
    res = Login.objects.filter(username=usn, password=psd)
    if res.exists():
        loginid=res[0].id
        request.session['logid']=loginid
        request.session['head'] = ""
        if res[0].usertype == 'admin':
            return redirect('/adminhome')
        elif res[0].usertype == 'trainer':
            return redirect('/trainerhome')
        elif res[0].usertype == 'shop':
            return redirect('/shophome')
        else:
            return HttpResponse('<script>alert("invalid ");window.location="/"</script>')
    else:
        return HttpResponse('<script>alert("does not exists");window.location="/"</script>')

def logout(request):
    request.session['logid'] =''
    return HttpResponse('<script>alert("logout");window.location="/"</script>')

def changepassword(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        return render(request, 'admin/changepassword.html')

def changepassword_post(request):
    cp=request.POST['textfield']
    np=request.POST['textfield2']
    conp=request.POST['textfield3']
    log=Login.objects.filter(id=request.session['logid'],password=cp)
    if log.exists():
       if np == conp:
           Login.objects.filter(id=request.session['logid']).update(password=conp)
           return HttpResponse('<script>alert("password changed");window.location="/adminhome"</script>')
       else:
           return HttpResponse('<script>alert("check your password");window.location="/adminhome"</script>')

    else:
        return HttpResponse('<script>alert("invalid ");window.location="/adminhome"</script>')



def adminhome(request):
    return render(request, 'admin/adminindex.html')

def addtrainer(request):
    # request.session['head'] = "ADD TRAINER"
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        return render(request, 'admin/addtrainer.html')


def addtrainer_post(request):
    trn=request.POST['textfield']
    eml=request.POST['textfield2']
    phn=request.POST['textfield3']
    plc=request.POST['textfield4']
    pst=request.POST['textfield5']
    pn=request.POST['textfield6']
    lat=request.POST['textfield7']
    lon=request.POST['textfield8']
    # ps=request.POST['textfieldp']
    import random
    # ps=request.POST['textfield7']
    # ps=random.randint(0000,9999)
    import smtplib




    log=Login.objects.filter(username=eml)
    if log.exists():
        return HttpResponse('<script>alert("already exists");window.location="/addtrainer"</script>')
    else:
        obj1=Login()
        obj1.username=eml
        obj1.password=eml
        obj1.usertype='trainer'
        obj1.save()
        obj=Trainer()
        obj.username=trn
        obj.email=eml
        obj.phone=phn
        obj.place=plc
        obj.post=pst
        obj.pin=pn
        obj.latitude=lat
        obj.longitude=lon
        obj.LOGIN=obj1
        # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # s.starttls()
        # s.login("fitwellproject@yahoo.com", "mriduljeevanmuza")
        # # s.login("projectfitwell@gmail.com", "ukgj crsc ohdr hlrk")
        # msg = MIMEMultipart()  # create a message.........."
        # msg['From'] = "fitwellproject@yahoo.com"
        # # msg['From'] = "projectfitwell@gmail.com"
        # msg['To'] = eml
        # msg['Subject'] = "Login Credentials for FITWELL Website!"
        # body = "Your Password is:- - " + str(ps)+"\n" + "your username is:- -" + str(eml)
        # msg.attach(MIMEText(body, 'plain'))
        # s.send_message(msg)
        obj.save()
        return HttpResponse('<script>alert("added successfully ");window.location="/adminhome"</script>')



def viewtrainer(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data1=Trainer.objects.all()
        return render(request, 'admin/viewtrainer.html',{'data1':data1})

def edittrainer(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data = Trainer.objects.get(id=id)
        return render(request, 'admin/edit_trainer.html',{'data':data,"id":id})

def edittrainer_post(request,id):
    trn=request.POST['textfield']
    phn=request.POST['textfield3']
    plc=request.POST['textfield4']
    pst=request.POST['textfield5']
    pn=request.POST['textfield6']
    lat=request.POST['textfield7']
    lon=request.POST['textfield8']
    Trainer.objects.filter(id=id).update(username=trn,phone=phn,place=plc,post=pst,pin=pn,latitude=lat,longitude=lon)
    return HttpResponse('<script>alert("added successfully ");window.location="/viewtrainer#admin"</script>')

def deletetrainer(request,id):
    Login.objects.get(id=id).delete()
    return HttpResponse('<script>alert("deleted successfully ");window.location="/viewtrainer#admin"</script>')


def addbatch(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        return render(request, 'admin/addbatch.html')

def addbatch_post(request):
    bn=request.POST['textfield']
    frtm=request.POST['textfield2']
    totm=request.POST['textfield3']
    obj=Batch()
    obj.Batchname=bn
    obj.Fromtime=frtm
    obj.Totime=totm
    obj.save()
    return HttpResponse('<script>alert("added successfully ");window.location="/addbatch#admin"</script>')

def viewbatch(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data2=Batch.objects.all()
        return render(request, 'admin/viewbatch.html',{'data2':data2})

def editbatch(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data = Batch.objects.get(id=id)
        return render(request, 'admin/edit_batch.html',{'data':data,"id":id})

def editbatch_post(request,id):
    bn=request.POST['textfield']
    frtm=request.POST['textfield2']
    totm=request.POST['textfield3']
    Batch.objects.filter(id=id).update(Batchname=bn,Fromtime=frtm,Totime=totm)
    return HttpResponse('<script>alert("added successfully ");window.location="/viewbatch"</script>')

def deletebacth(request,id):
    Batch.objects.get(id=id).delete()
    return HttpResponse('<script>alert("deleted successfully ");window.location="/viewbatch#admin"</script>')

# def uploadmealplans(request):
#     if request.session['logid'] == '':
#         return HttpResponse('<script>alert("logout");window.location="/"</script>')
#     else:
#         return render(request, 'admin/uploadmealplans.html')

# def uploadmealplans_post(request):
#     # obj1=Trainer.objects.get(LOGIN=request.session['logid'])
#     cat=request.POST['select']
#     day=request.POST['textfield']
#     bf=request.POST['textfield2']
#     lch=request.POST['textfield3']
#     dnr=request.POST['textfield4']
#     obj=Diet()
#     # obj.TRAINER=obj1
#     obj.category=cat
#     obj.day=day
#     obj.breakfast=bf
#     obj.lunch=lch
#     obj.dinner=dnr
#     obj.save()
#     return HttpResponse('<script>alert("added successfully ");window.location="/uploadmealplans"</script>')
#
# def viewmealplans(request):
#     # obj1 = Trainer.objects.get(LOGIN=request.session['logid'])
#     # data=Diet.objects.filter(TRAINER=obj1)
#     data=Diet.objects.all()
#     if request.session['logid'] == '':
#         return HttpResponse('<script>alert("logout");window.location="/"</script>')
#     else:
#         return render(request, 'admin/viewmealplans.html', {'data':data})
#
# def editmealplans(request,id):
#     data=Diet.objects.get(id=id)
#     if request.session['logid'] == '':
#         return HttpResponse('<script>alert("logout");window.location="/"</script>')
#     else:
#         return render(request, 'admin/editmealplans.html',{'data':data})
#
# def editmealplans_post(request,id):
#     cat=request.POST['select']
#     day=request.POST['textfield']
#     bf=request.POST['textfield2']
#     lch=request.POST['textfield3']
#     dnr=request.POST['textfield4']
#     Diet.objects.filter(id=id).update(category=cat,day=day,breakfast=bf,lunch=lch,dinner=dnr)
#     return HttpResponse('<script>alert("added successfully ");window.location="/viewmealplans"</script>')
#
# def deletemealplans(request,id):
#     Diet.objects.get(id=id).delete()
#     return HttpResponse('<script>alert("deleted successfully ");window.location="/viewmealplans"</script>')

def allocatetrainer(request,id):
    # obj=Batch.objects.get(id=id)
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Trainer.objects.all()
        data1=Batch.objects.all()
        return render(request, 'admin/allocatetrainer.html',{'data':data,'data1':data1,'id':id})

def allocation_post(request,id):
    # obj = Batch.objects.get(id=id)
    sel=request.POST['select']
    sel1=request.POST['select1']
    dt=request.POST['textfield']
    # tm=request.POST['textfield1']

    data=Allocate.objects.filter(TRAINER=sel,BATCH=sel1)
    if data.exists():
        return HttpResponse('<script>alert("already allocated ");window.location="/approvedrequest"</script>')
    else:
        obj1=Allocate()
        obj1.REQUEST_id=id
        obj1.TRAINER_id=sel
        obj1.BATCH_id=sel1
        # obj1.Time=tm
        obj1.date=dt
        obj1.save()
        return HttpResponse('<script>alert("allocated successfully ");window.location="/approvedrequest"</script>')


def complaint(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Complaint.objects.all()
        return render(request, 'admin/complaint.html',{'data':data})

def rating(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data = Rating.objects.all()
        return render(request, 'admin/viewraiting.html',{'data':data})

def admin_viewrating(request, id):
    if request.session['logid'] == "":
        return HttpResponse('<script>alert("logout Successfully");window.location="/login"</script>')
    else:
        obj=Rating.objects.filter(TRAINER=id)
        fs = "/static/star/full.jpg"
        hs = "/static/star/half.jpg"
        es = "/static/star/empty.jpg"
        data = []

        for rt in obj:
            a = float(rt.rating)

            if a >= 0.0 and a < 0.4:
                print("eeeee")
                ar = [es, es, es, es, es]

            elif a >= 0.4 and a < 0.8:
                print("heeee")
                ar = [hs, es, es, es, es]

            elif a >= 0.8 and a < 1.4:
                print("feeee")
                ar = [fs, es, es, es, es]

            elif a >= 1.4 and a < 1.8:
                print("fheee")
                ar = [fs, hs, es, es, es]

            elif a >= 1.8 and a < 2.4:
                print("ffeee")
                ar = [fs, fs, es, es, es]

            elif a >= 2.4 and a < 2.8:
                print("ffhee")
                ar = [fs, fs, hs, es, es]

            elif a >= 2.8 and a < 3.4:
                print("fffee")
                ar = [fs, fs, fs, es, es]


            elif a >= 3.4 and a < 3.8:
                print("fffhe")
                ar = [fs, fs, fs, hs, es]


            elif a >= 3.8 and a < 4.4:
                print("ffffe")
                ar = [fs, fs, fs, fs, es]


            elif a >= 4.4 and a < 4.8:
                print("ffffh")
                ar = [fs, fs, fs, fs, hs]


            elif a >= 4.8 and a <= 5.0:
                print("fffff")
                ar = [fs, fs, fs, fs, fs]
                data.append({""})
            data.append({"name": rt.USER.username,
                         "date": rt.date,
                         "rating": ar})

        # return render_template('admin/adm_view_apprating.html',data=re33,r1=ar,ln=len(ar55))
        print(data)

        return render(request,'admin/viewraiting.html', {"data": data})

def send_reply(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Complaint.objects.get(id=id)
        return render(request, 'admin/reply.html',{'data':data})

def send_reply_post(request,id):
    rpl=request.POST['textarea']
    dt=datetime.datetime.now().strftime('%Y-%m-%d')
    Complaint.objects.filter(id=id).update(reply=rpl,replydate=dt)
    return HttpResponse('<script>alert("replied successfully ");window.location="/complaint#admin"</script>')

def viewfeedback(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Feedback.objects.all()
        return render(request, 'admin/viewfeedback.html',{'data':data})

def viewrequestfromuser(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Requestt.objects.filter(requeststatus='pending')
        return render(request, 'admin/viewrequestfromuser.html',{'data':data})

def approverequest(request,id):
    Requestt.objects.filter(id=id).update(requeststatus='approved')
    return HttpResponse('<script>alert("approved successfully ");window.location="/viewrequestfromuser"</script>')

def rejectrequest(request,id):
    Requestt.objects.filter(id=id).update(requeststatus='rejected')
    return HttpResponse('<script>alert("rejected successfully ");window.location="/viewrequestfromuser"</script>')

def approvedrequest(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Requestt.objects.filter(requeststatus='approved')
        return render(request, 'admin/approvedrequest.html',{'data':data})

def viewshops(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Shops.objects.filter(LOGIN__usertype='pending')
        return render(request, 'admin/viewshops.html',{'data':data})

def approveshops(request,id):
    Login.objects.filter(id=id).update(usertype='shop')
    return HttpResponse('<script>alert("approved successfully ");window.location="/viewshops#admin"</script>')

def rejectshops(request,id):
    Login.objects.filter(id=id).update(usertype='rejected')
    return HttpResponse('<script>alert("shop rejected ");window.location="/viewshops#admin"</script>')

def approvedshop(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Shops.objects.filter(LOGIN__usertype='shop')
        return render(request, 'admin/approvedshop.html',{'data':data})


# ===========================================TRAINER===================================================================================================================





def trainerhome(request):
        return render(request, 'trainer/trainerindex.html')

def viewtrainerprofile(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Trainer.objects.get(LOGIN=request.session['logid'])
        return render(request, 'trainer/viewtrainerprofile.html', {'data':data})

def edittrainerprofile(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data = Trainer.objects.get(id=id)
        return render(request, 'trainer/editprofile.html',{'data':data,"id":id})

def edittrainerprofile_post(request,id):
    trn=request.POST['textfield']
    phn=request.POST['textfield3']
    plc=request.POST['textfield4']
    pst=request.POST['textfield5']
    pn=request.POST['textfield6']
    lat=request.POST['textfield7']
    lon=request.POST['textfield8']
    Trainer.objects.filter(id=id).update(username=trn,phone=phn,place=plc,post=pst,pin=pn,latitude=lat,longitude=lon)
    return HttpResponse('<script>alert("added successfully ");window.location="/viewtrainerprofile#adminvi"</script>')

def viewallocation(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        obj=Trainer.objects.get(LOGIN=request.session['logid'])
        data=Allocate.objects.filter(TRAINER=obj)
        return render(request, 'trainer/viewallocation.html', {'data':data})

def viewuser(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=User.objects.get(id=id)
        try:
            obj=Health.objects.get(USER=id)
            request.session['uid'] = id
            return render(request, 'trainer/viewuser.html', {'data':data,'obj':obj})
        except Exception as e:
            request.session['uid'] = id
            return render(request, 'trainer/viewuser.html', { 'data': data})


def trainer_changepassword(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        return render(request, 'trainer/changepassword.html')

def trainer_changepassword_post(request):
    cp=request.POST['textfield']
    np=request.POST['textfield2']
    conp=request.POST['textfield3']
    log=Login.objects.filter(id=request.session['logid'],password=cp)
    if log.exists():
       if np == conp:
           Login.objects.filter(id=request.session['logid']).update(password=conp)
           return HttpResponse('<script>alert("password changed");window.location="/trainerhome"</script>')
       else:
           return HttpResponse('<script>alert("check your password");window.location="/trainerhome"</script>')

    else:
        return HttpResponse('<script>alert("invalid ");window.location="/trainerhome"</script>')

def addworkout(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        return render(request, 'trainer/addworkout.html')

def addworkout_post(request):
    obj1=Trainer.objects.get(LOGIN=request.session['logid'])
    wrkn=request.POST['textfield']
    cat=request.POST['textfield2']
    dura=request.POST['textfield3']
    exrs=request.POST['textarea']
    sets=request.POST['textfield4']
    reps=request.POST['textfield5']
    rest=request.POST['textfield6']
    obj=Workout()
    obj.TRAINER=obj1
    obj.workoutname=wrkn
    obj.category=cat
    obj.duration=dura
    obj.exercise=exrs
    obj.sets=sets
    obj.reps=reps
    obj.resttime=rest
    obj.save()
    return HttpResponse('<script>alert("added successfully ");window.location="/addworkout"</script>')

def viewworkout(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        obj1=Trainer.objects.get(LOGIN=request.session['logid'])
        data=Workout.objects.filter(TRAINER=obj1)
        return render(request, 'trainer/viewworkout.html', {'data':data})

# def viewexercise(request):
#     if request.session['logid'] == '':
#         return HttpResponse('<script>alert("logout");window.location="/"</script>')
#     else:
#         obj1=Trainer.objects.get(LOGIN=request.session['logid'])
#         # data=Workout.objects.filter(TRAINER=obj1)
#         return render(request, 'trainer/viewexercise.html', {'data':data})

def viewexercise(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        # obj1=Trainer.objects.get(LOGIN=request.session['logid'])
        # data=Workout.objects.filter(TRAINER=obj1)
        data=Workout.objects.get(id=id)
        request.session['tid']=id
        return render(request, 'trainer/viewexercise.html', {'data':data})

def editworkout(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Workout.objects.get(id=id)
        return render(request, 'trainer/editworkout.html',{'data':data,"id":id})

def editworkout_post(request,id):
    wrkn=request.POST['textfield']
    cat=request.POST['textfield2']
    dura=request.POST['textfield3']
    exrs=request.POST['textarea']
    sets=request.POST['textfield4']
    reps=request.POST['textfield5']
    rest=request.POST['textfield6']
    Workout.objects.filter(id=id).update(workoutname=wrkn,category=cat,duration=dura,exercise=exrs,sets=sets,reps=reps,resttime=rest)
    return HttpResponse('<script>alert("added successfully ");window.location="/viewworkout"</script>')

def deleteworkout(request,id):
    Workout.objects.get(id=id).delete()
    return HttpResponse('<script>alert("deleted successfully ");window.location="/viewworkout"</script>')

def addtips(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        return render(request, 'trainer/addtips.html',{'id':id})

def addtips_post(request,id):
    tps=request.POST['textarea']
    uid=request.session['uid']
    obj1 = Trainer.objects.get(LOGIN=request.session['logid'])
    obj=Tips()
    obj.TRAINER=obj1
    obj.USER_id=id
    obj.tips=tps
    obj.save()
    return HttpResponse('<script>alert("added successfully ");window.location="/viewuser/'+uid+'"</script>')

def edittips(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Tips.objects.get(id=id)
        return render(request, 'trainer/edittips.html',{'data':data,"id":id})

def edittips_post(request,id):
    tps=request.POST['textarea']
    Tips.objects.filter(id=id).update(tips=tps)
    tid=request.session['tid']
    return HttpResponse('<script>alert("added successfully ");window.location="/viewtips/'+tid+'"</script>')

def deletetips(request,id):
    Tips.objects.get(id=id).delete()
    tid=request.session['tid']
    return HttpResponse('<script>alert("deleted successfully ");window.location="/viewtips/'+tid+'"</script>')

def viewtips(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Tips.objects.filter(USER_id=id)
        request.session['tid'] = id
        return render(request, 'trainer/viewtips.html', {'data':data})

def uploadmealplans(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        return render(request, 'trainer/uploadmealplans.html')

def uploadmealplans_post(request):
    obj1=Trainer.objects.get(LOGIN=request.session['logid'])
    cat=request.POST['textfield0']
    day=request.POST['textfield']
    bf=request.POST['textfield2']
    lch=request.POST['textfield3']
    dnr=request.POST['textfield4']
    obj=Diet()
    obj.TRAINER=obj1
    obj.category=cat
    obj.day=day
    obj.breakfast=bf
    obj.lunch=lch
    obj.dinner=dnr
    obj.save()
    return HttpResponse('<script>alert("added successfully ");window.location="/uploadmealplans"</script>')

def viewmealplans(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        obj1 = Trainer.objects.get(LOGIN=request.session['logid'])
        data=Diet.objects.filter(TRAINER=obj1)
        return render(request, 'trainer/viewmealplans.html', {'data':data})

def editmealplans(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Diet.objects.get(id=id)
        return render(request, 'trainer/editmealplans.html',{'data':data})

def editmealplans_post(request,id):
    cat=request.POST['textfield0']
    day=request.POST['textfield']
    bf=request.POST['textfield2']
    lch=request.POST['textfield3']
    dnr=request.POST['textfield4']
    Diet.objects.filter(id=id).update(category=cat,day=day,breakfast=bf,lunch=lch,dinner=dnr)
    return HttpResponse('<script>alert("added successfully ");window.location="/viewmealplans"</script>')

def deletemealplans(request,id):
    Diet.objects.get(id=id).delete()
    return HttpResponse('<script>alert("deleted successfully ");window.location="/viewmealplans"</script>')

def viewrating(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Trainer.objects.get(LOGIN=request.session['logid'])
        obj=Rating.objects.filter(TRAINER=data)
        # obj = Rating.objects.filter(TRAINER=id)
        fs = "/static/star/full.jpg"
        hs = "/static/star/half.jpg"
        es = "/static/star/empty.jpg"
        data = []

        for rt in obj:
            a = float(rt.rating)
            ar=[]
            if a >= 0.0 and a < 0.4:
                print("eeeee")
                ar = [es, es, es, es, es]

            elif a >= 0.4 and a < 0.8:
                print("heeee")
                ar = [hs, es, es, es, es]

            elif a >= 0.8 and a < 1.4:
                print("feeee")
                ar = [fs, es, es, es, es]

            elif a >= 1.4 and a < 1.8:
                print("fheee")
                ar = [fs, hs, es, es, es]

            elif a >= 1.8 and a < 2.4:
                print("ffeee")
                ar = [fs, fs, es, es, es]

            elif a >= 2.4 and a < 2.8:
                print("ffhee")
                ar = [fs, fs, hs, es, es]

            elif a >= 2.8 and a < 3.4:
                print("fffee")
                ar = [fs, fs, fs, es, es]


            elif a >= 3.4 and a < 3.8:
                print("fffhe")
                ar = [fs, fs, fs, hs, es]


            elif a >= 3.8 and a < 4.4:
                print("ffffe")
                ar = [fs, fs, fs, fs, es]


            elif a >= 4.4 and a < 4.8:
                print("ffffh")
                ar = [fs, fs, fs, fs, hs]


            elif a >= 4.8 and a <= 5.0:
                print("fffff")
                ar = [fs, fs, fs, fs, fs]
                data.append({""})
            data.append({"name": rt.USER.username,
                         "date": rt.date,
                         "rating": ar})

        # return render_template('admin/adm_view_apprating.html',data=re33,r1=ar,ln=len(ar55))
        print(data)

        return render(request, 'trainer/viewrating.html', {'data':data})



def add_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    message = request.POST['message']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    t=datetime.datetime.now().strftime("%H:%m:%d")
    expid = Trainer.objects.get(id=toid)
    uid = User.objects.get(LOGIN=lid)
    obj=Chat()
    obj.date=d
    obj.time=t
    obj.type='user'
    obj.TRAINER=expid
    obj.USER=uid
    obj.chat=message
    obj.save()
    return JsonResponse({'status':"Inserted"})

def view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    lastid = request.POST['lastid']
    print("kkkkkkkkkk",lid,toid,lastid)
    # res=Chat.objects.filter(USER=User.objects.get(LOGIN=lid))
    res=Chat.objects.filter(Q(USER=User.objects.get(LOGIN=lid)),Q(id__gt=lastid))
    print("hhhhhhhhhhhhh",res)
    ar=[]
    for i in res:
        print("i.id",i.id)
        ar.append({
            "id":i.id,
            "date":i.date,
            "userid":i.USER.id,
            "sid":i.type,
            "chat":i.chat,
        })
    print(ar,"arrrrrrrrrrr")
    return JsonResponse({'status':"ok",'data':ar})


# =======web=========

def chatt(request,u):
    request.session['head']="CHAT"
    request.session['uid'] = u
    return render(request,'trainer/chat.html',{'u':u})


def chatsnd(request,u):
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        # t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['logid']
        b=request.POST['n']
        print(b)
        print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc = Trainer.objects.get(LOGIN__id=c)
        # uu = user.objects.get(id=request.session['uid'])
        obj=Chat()
        obj.date=d
        obj.type='trainer'
        obj.TRAINER=cc
        obj.USER_id=u
        obj.chat=m
        obj.save()
        print(obj)
        v = {}
        if int(obj) > 0:
            v["status"] = "ok"
        else:
            v["status"] = "error"
        r = JsonResponse.encode(v)
        return r
    # else:
    #     return redirect('/')

def chatrply(request):
    # if request.session['log']=="lo":
        c = request.session['logid']
        cc=Trainer.objects.get(LOGIN__id=c)
        uu=User.objects.get(id=request.session['uid'])
        res = Chat.objects.filter(TRAINER=cc,USER=uu)
        print(res)
        v = []
        if len(res) > 0:
            print(len(res))
            for i in res:
                v.append({
                    'type':i.type,
                    'chat':i.chat,
                    'name':i.USER.username,
                    # 'upic':i.USER.photo,
                    'dtime':i.date,
                    'tname':i.TRAINER.username,
                })
            # print(v)
            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})






# ===========================================SHOP===================================================================================================================


def shophome(request):
    return render(request, 'shop/shopindex.html')


def registration(request):
        return render(request, 'shop/registration.html')

def registration_post(request):
    sn = request.POST['textfield']
    em = request.POST['textfield2']
    pwd = request.POST['textfieldp']
    cno = request.POST['textfield3']
    pl = request.POST['textfield4']
    pst = request.POST['textfield5']
    pn = request.POST['textfield6']
    ot = request.POST['textfield7']
    ct = request.POST['textfield8']
    lat = request.POST['textfield9']
    long = request.POST['textfield10']
    log=Login()
    log.username=em
    log.password=pwd
    log.usertype='pending'
    log.save()
    obj=Shops()
    obj.LOGIN=log
    obj.shopname=sn
    obj.email=em
    obj.password=pwd
    obj.contactno=cno
    obj.place=pl
    obj.post=pst
    obj.pin=pn
    obj.openingtime=ot
    obj.closingtime=ct
    obj.latitude=lat
    obj.longitude=long
    obj.save()
    return HttpResponse('<script>alert("registered successfully ");window.location="/"</script>')

def viewshopprofile(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Shops.objects.get(LOGIN=request.session['logid'])
        return render(request, 'shop/viewshopprofile.html', {'data':data})

def editshopprofile(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data = Shops.objects.get(id=id)
        return render(request, 'shop/editshopprofile.html',{'data':data,"id":id})

def editshopprofile_post(request,id):
    sn = request.POST['textfield']
    # em = request.POST['textfield2']
    # pwd = request.POST['textfieldp']
    cno = request.POST['textfield3']
    pl = request.POST['textfield4']
    pst = request.POST['textfield5']
    pn = request.POST['textfield6']
    ot = request.POST['textfield7']
    ct = request.POST['textfield8']
    lat = request.POST['textfield9']
    long = request.POST['textfield10']
    Shops.objects.filter(id=id).update(shopname=sn,contactno=cno,place=pl,post=pst,pin=pn,latitude=lat,longitude=long,openingtime=ot,closingtime=ct)
    return HttpResponse('<script>alert("added successfully ");window.location="/viewshopprofile"</script>')

def addproduct(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        return render(request, 'shop/addproduct.html')

def addproduct_post(request):
    obj1=Shops.objects.get(LOGIN=request.session['logid'])
    pn=request.POST['textfield']
    pd=request.POST['textarea']
    img=request.FILES['fileField']
    prc=request.POST['textfield2']
    date=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs=FileSystemStorage()
    fs.save(r"C:\Users\asika\Downloads\fitwellzip23_1_24vr2.0\untitled1\FitWell\static\images\\"+date+'.jpg',img)
    path="/static/images/"+date+'.jpg'
    obj=Product()
    obj.SHOP=obj1
    obj.itemname=pn
    obj.itemdescription=pd
    obj.image=path
    obj.price=prc
    obj.save()
    return HttpResponse('<script>alert("added successfully ");window.location="/shophome"</script>')



def viewproducts(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        obj1=Shops.objects.get(LOGIN=request.session['logid'])
        data=Product.objects.filter(SHOP=obj1)
        return render(request, 'shop/viewproducts.html', {'data':data})

def editproducts(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Product.objects.get(id=id)
        return render(request, 'shop/editproducts.html',{'data':data})

def editproducts_post(request,id):
   try:
        pn=request.POST['textfield']
        pd=request.POST['textarea']
        img=request.FILES['fileField']
        prc=request.POST['textfield2']
        date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\asika\Downloads\fitwellzip23_1_24vr2.0\untitled1\FitWell\static\images\\" + date + '.jpg', img)
        path = "/static/images/" + date + '.jpg'
        Product.objects.filter(id=id).update(itemname=pn,itemdescription=pd,image=path,price=prc)
        return HttpResponse('<script>alert("added successfully ");window.location="/viewproducts"</script>')
   except Exception as e:
        pn=request.POST['textfield']
        pd=request.POST['textarea']
        prc=request.POST['textfield2']
        Product.objects.filter(id=id).update(itemname=pn,itemdescription=pd,price=prc)
        return HttpResponse('<script>alert("added successfully ");window.location="/viewproducts"</script>')


# def editproducts_post(request, id):
#     if request.method == 'POST':
#         pn = request.POST['textfield']
#         pd = request.POST['textarea']
#         prc = request.POST['textfield2']
#
#         # Handle the image upload
#         img = request.FILES['fileField'] if 'fileField' in request.FILES else None
#         if img is not None:
#             file_name = default_storage.save(img.name, img)
#             img = default_storage.url(file_name)
#
#         Product.objects.filter(id=id).update(itemname=pn, itemdescription=pd, image=img, price=prc)
#         return HttpResponse('<script>alert("added successfully ");window.location="/viewproducts"</script>')

def deleteproduct(request,id):
    Product.objects.get(id=id).delete()
    return HttpResponse('<script>alert("deleted successfully ");window.location="/viewproducts"</script>')

def orderrequest(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        datas=[]
        data=Shops.objects.get(LOGIN=request.session['logid'])
        qry=Order.objects.filter(SHOP=data,status="payment")
        for i in qry:
            sum = 0

            q=Ordersub.objects.filter(ORDER=i.id)
            for k in q:
                total=int(k.quantity)*int(k.PRODUCT.price)
                print("tttttttttt:",total)
                sum=int(sum)+int(total)
            datas.append({
                "id":i.id,
                "paymentstatus":i.paymentstatus,
                "paymentdate":i.paymentdate,
                # "name": k.PRODUCT.itemname,
                "user":i.USER.username,
                "up":str(i.USER.phone),
                "date":i.date,
                "sum":sum
            })


        return render(request, 'shop/orderrequest.html',{'data':datas})

def approveorder(request,id):
    Order.objects.filter(id=id).update(status='approved')
    return HttpResponse('<script>alert("approved successfully ");window.location="/orderrequest"</script>')

def rejectorder(request,id):
    Order.objects.filter(id=id).update(status='rejected')
    return HttpResponse('<script>alert("rejected successfully ");window.location="/orderrequest"</script>')

def vieworder(request,id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Ordersub.objects.filter(ORDER=id)
        arr = []
        for i in data:
            arr.append({"name": i.PRODUCT.itemname,
                        "description": i.PRODUCT.itemdescription,
                        "image": i.PRODUCT.image,
                        "quantity": i.quantity,
                        "price": float(i.quantity)*float(i.PRODUCT.price)})
        return render(request, 'shop/ordersub.html',{'data':arr})

def viewapprovedorder(request):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Shops.objects.get(LOGIN=request.session['logid'])
        obj=Order.objects.filter(SHOP=data,status='approved')
        return render(request, 'shop/viewapprovedorder.html',{'data':obj})



def viewpayment(request):
    # if request.session['logid'] == '':
    #     return HttpResponse('<script>alert("logout");window.location="/"</script>')
    # else:
    #     date = datetime.datetime.now().strftime('%Y-%m-%d')
    #     data=Order.objects.filter(SHOP__LOGIN=request.session['logid'],paymentdate__lt=date)
    #     return render(request, 'shop/viewpayment.html', {'data':data})
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        datas=[]
        data=Shops.objects.get(LOGIN=request.session['logid'])
        qry=Order.objects.filter(SHOP=data,status="payment")
        for i in qry:
            sum = 0

            q=Ordersub.objects.filter(ORDER=i.id)
            for k in q:
                total=int(k.quantity)*int(k.PRODUCT.price)
                print("tttttttttt:",total)
                sum=int(sum)+int(total)
            datas.append({
                "id":i.id,
                "paymentstatus":i.paymentstatus,
                "paymentdate":i.paymentdate,
                "user":i.USER.username,
                # "up":str(i.USER.phone),
                # "date":i.date,
                # "sum":sum
            })


        return render(request, 'shop/viewpayment.html',{'data':datas})



def viewpaymentdetails(request, id):
    if request.session['logid'] == '':
        return HttpResponse('<script>alert("logout");window.location="/"</script>')
    else:
        data=Ordersub.objects.filter(ORDER=id)
        arr = []
        for i in data:
            arr.append({"name": i.PRODUCT.itemname,
                        "description": i.PRODUCT.itemdescription,
                        "image": i.PRODUCT.image,
                        "quantity": i.quantity,
                        "price": float(i.quantity)*float(i.PRODUCT.price)})
        return render(request, 'shop/viewpaymentdetails.html',{'data':arr})


# def viewpaymenthistory(request):
#
#         return render(request, 'shop/viewpaymenthistory.html')

def viewpaymenthistory(request):
    try:
        yr = request.POST['year']
        mo = request.POST['month']
        d = yr + "-" + mo
        price = 0
        print(d)
        data = Order.objects.filter(SHOP__LOGIN=request.session['logid'], date__contains=d)
        for i in data:
            sub = Ordersub.objects.filter(ORDER=i.id)
            for j in sub:
                pr = int(j.PRODUCT.price)
                amt = int(j.quantity)
                price += pr * amt
        daa = {'date': d, 'amt': price}
        print(daa)
        return render(request, 'shop/viewpaymenthistory.html', {'data': daa})
    except Exception as e:
        data = Order.objects.filter(SHOP__LOGIN=request.session['logid'])
        print(data)
        return render(request, 'shop/viewpaymenthistory.html', {'data': data})


# def viewproduct(request,id):
#     if request.session['logid'] == '':
#         return HttpResponse('<script>alert("logout");window.location="/"</script>')
#     else:
#         data=Product.objects.get(LOGIN=request.session['logid'])
#         return render(request, 'shop/viewproduct.html',{'data':data})


# ===========================Android===================================================================================================

# def and_login(request):
#     u=request.POST['uname']
#     p=request.POST['upass']
#     log=Login.objects.filter(username=u,password=p)
#     if log.exists():
#         lid=log[0].id
#         type=log[0].usertype
#
#     return JsonResponse({"status":"ok","type":'type',"lid":'lid'})


def and_login(request):
    u = request.POST['uname']
    p = request.POST['upass']
    log = Login.objects.filter(username=u, password=p)
    print(log)
    if log.exists():
        lid = log[0].id
        type = log[0].usertype

        return JsonResponse({"status": "ok", "type":type, "lid":lid})
    else:
        return JsonResponse({"status": "non"})

def and_view_products(request):
    sid=request.POST['sid']
    pr=Product.objects.filter(SHOP=sid)
    ary=[]
    for i in pr:
        ary.append({
            "id":i.id,
            "name":i.itemname,
            "image":i.image,
            "description":i.itemdescription,
            "price":i.price
        })
    if len(ary)>0:
        return JsonResponse({"status": "ok", "data":ary })
    else:
        return JsonResponse({"status":"no"})

def and_view_batch(request):
    pr=Batch.objects.all()
    if pr.exists():
        ary=[]
        for i in pr:
            ary.append({
                "id":i.id,
                "bn":i.Batchname,
                "ft":i.Fromtime,
                "tt":i.Totime
            })
        return JsonResponse({"status": "ok", "data":ary })

def and_view_reply(request):
    rp=Complaint.objects.filter(USER__LOGIN=request.POST['lid'])
    if rp.exists():
        ary=[]
        for i in rp:
            ary.append({
                "id":i.id,
                "comp":i.complaints,
                "rep":i.reply
            })
        return JsonResponse({"status": "ok", "data":ary })

def and_view_shops(request):
    sp=Shops.objects.filter(LOGIN__usertype="shop")
    if sp.exists():
        ary=[]
        for i in sp:
            ary.append({
                "id":i.id,
                "shopname":i.shopname,
                "email":i.email,
                "con":i.contactno,
                "place":i.place,
                "opt":i.openingtime,
                "clt":i.closingtime
            })
        return JsonResponse({"status": "ok", "data":ary })

def and_view_tips(request):
    tid=request.POST['tid']
    sp=Tips.objects.filter(TRAINER=tid)
    if sp.exists():
        ary=[]
        for i in sp:
            ary.append({
                "id":i.id,
                "tn":i.TRAINER.username,
                "tps":i.tips,
            })
        return JsonResponse({"status": "ok", "data":ary })
    else:
        return JsonResponse({"status": "no"})


def and_view_workouts(request):
    lid = request.POST['lid']
    ary = []
    a = Allocate.objects.filter(REQUEST__USER__LOGIN=lid)
    for i in a:
        wr=Workout.objects.filter(TRAINER=i.TRAINER_id)
        if wr.exists():

            for i in wr:
                ary.append({
                    "id":i.id,
                    "wn":i.workoutname,
                    "cat":i.category,
                    "dura":i.duration,
                    "exer":i.exercise,
                    "sets":i.sets,
                    "reps":i.reps,
                    "rest":i.resttime,
                })
    return JsonResponse({"status": "ok", "data":ary })

def and_view_meal_plans(request):
    ml=Diet.objects.all()
    if ml.exists():
        ary=[]
        for i in ml:
            ary.append({
                "id":i.id,
                "cat":i.category,
                "day":i.day,
                "brf":i.breakfast,
                "lun":i.lunch,
                "dn":i.dinner,
            })
            print(ary)
        return JsonResponse({"status": "ok", "data":ary })

def and_view_cart(request):
    lid=request.POST['lid']
    ca=Cart.objects.filter(USER__LOGIN=lid)
    sum=0
    ary=[]
    for i in ca:
        total=int(i.quantity)*int(i.PRODUCT.price)
        sum=sum+total
        ary.append({
            "id":i.id,
            "pr":i.PRODUCT.itemname,
            "img":i.PRODUCT.image,
            "qn":i.quantity,
            "prc":i.PRODUCT.price,
            "tl":total,
            "shnfo":i.PRODUCT.SHOP.shopname+"\n"+str(i.PRODUCT.SHOP.contactno)

        })
    if len(ary)>0:
        return JsonResponse({"status": "ok", "data":ary,"sum":sum })
    else:
        return JsonResponse({"status":"no"})

def and_user_register(request):
    name=request.POST['uname']
    email=request.POST['email']
    password=request.POST['upass']
    phone=request.POST['phone']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    gender=request.POST['gender']

    log=Login()
    log.username=email
    log.password=password
    log.usertype='user'
    log.save()

    reg=User()
    reg.LOGIN=log
    reg.username=name
    reg.gender=gender
    reg.email=email
    reg.phone=phone
    reg.place=place
    reg.post=post
    reg.pin=pin
    reg.save()
    return JsonResponse({"status":"ok"})

def and_user_send_request(request):
    requests=request.POST['requests']
    lid=request.POST['lid']
    print("lid",lid)
    bid=request.POST['bid']
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    time= datetime.datetime.now().strftime("%H:%M:5S")
    obj=Requestt.objects.filter(USER=User.objects.get(LOGIN=lid),BATCH=bid)
    if obj.exists():
        return JsonResponse({"status": "non"})
    else:
        req=Requestt()
        req.USER=User.objects.get(LOGIN=lid)
        req.BATCH_id=bid
        req.date=date
        req.time=time
        req.requeststatus="pending"
        req.note=requests
        req.save()
        return JsonResponse({"status":"ok"})

def and_add_health_details(request):
    # requests=request.POST['requests']
    lid=request.POST['lid']
    height=request.POST['height']
    weight=request.POST['weight']
    allergies=request.POST['allergies']
    medical=request.POST['medical']
    if Health.objects.filter(USER=User.objects.get(LOGIN=lid)).exists():
        h = Health.objects.get(USER=User.objects.get(LOGIN=lid))
        h.USER = User.objects.get(LOGIN=lid)
        h.height = height
        h.weight = weight
        h.alergies = allergies
        h.medicalhistory = medical
        h.save()
        return JsonResponse({"status":"Updated"})
    h=Health()
    h.USER=User.objects.get(LOGIN=lid)
    h.height=height
    h.weight=weight
    h.alergies=allergies
    h.medicalhistory=medical
    h.save()
    return JsonResponse({"status":"ok"})


def and_view_added_health(request):
    lid = request.POST['lid']
    data = Health.objects.get(USER=User.objects.get(LOGIN=lid))
    return JsonResponse(
        {"status": "ok", "height": data.height, "weight": data.weight, "alergies": data.alergies,
         "medicalhistory": data.medicalhistory})


def and_view_request_status(request):
    lid=request.POST['lid']
    req=Requestt.objects.filter(USER=User.objects.get(LOGIN=lid),requeststatus="approved")
    if req.exists():
        ary=[]
        for i in req:
            ary.append({
                "id":i.id,
                "bt":i.BATCH.Batchname,
                "req":i.note,
                "res":i.requeststatus,
            })
        return JsonResponse({"status": "ok", "data":ary })
    else:
        return JsonResponse({"status": "no"})


def and_view_trainer(request):
    lid=request.POST['lid']
    rid=request.POST['rid']
    print("rid",rid)
    req=Allocate.objects.filter(REQUEST=rid)
    if req.exists():
        ary=[]
        for i in req:
            ary.append({
                "id":i.TRAINER.id,
                "tn":i.TRAINER.username,
                "em":i.TRAINER.email,
                "ph":i.TRAINER.phone,
                "plc":i.TRAINER.place,
            })
        return JsonResponse({"status": "ok", "data":ary })
    return JsonResponse({"status": "ok","data":[] })

def send_feedback(request):
    lid=request.POST['lid']
    tid=request.POST['tid']
    feedback=request.POST['feedback']
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    time= datetime.datetime.now().strftime("%H:%M:%S")
    # obj=Feedback.objects.filter(USER=User.objects.get(LOGIN=lid))
    fd=Feedback()
    fd.feedback=feedback
    fd.date=date
    fd.Time=time
    fd.TRAINER_id = tid
    fd.USER_id = User.objects.get(LOGIN=lid).id
    fd.save()
    return JsonResponse({"status":"ok"})


def and_send_complaints(request):
    lid=request.POST['lid']
    # tid=request.POST['tid']
    complaints=request.POST['complaints']
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    cm=Complaint()
    cm.complaints=complaints
    cm.complaintdate=date
    # cm.TRAINER_id = tid
    cm.USER_id = User.objects.get(LOGIN=lid).id
    cm.save()
    return JsonResponse({"status":"ok"})






def and_send_rating(request):
    lid=request.POST['lid']
    tid=request.POST['tid']
    r=request.POST['r']
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    time= datetime.datetime.now().strftime("%H:%M:%S")
    # obj=Feedback.objects.filter(USER=User.objects.get(LOGIN=lid))
    if Rating.objects.filter(TRAINER_id = tid,USER_id = User.objects.get(LOGIN=lid).id).exists():
        fd = Rating.objects.get(TRAINER_id = tid,USER_id = User.objects.get(LOGIN=lid).id)
        fd.rating = r
        fd.date = date
        fd.TRAINER_id = tid
        fd.USER_id = User.objects.get(LOGIN=lid).id
        fd.save()
        return JsonResponse({"status": "ok"})

    fd=Rating()
    fd.rating=r
    fd.date=date
    fd.TRAINER_id = tid
    fd.USER_id = User.objects.get(LOGIN=lid).id
    fd.save()
    return JsonResponse({"status":"ok"})

def add_to_cart(request):
    lid=request.POST['lid']
    q=request.POST['quantity']
    pid=request.POST['pid']
    qry=Cart.objects.filter(USER__LOGIN=lid,PRODUCT=pid)
    if qry.exists():
        Cart.objects.filter(id=qry[0].id).update(quantity=int(qry[0].quantity)+int(q))
        return JsonResponse({"status":"no"})
    else:
        obj=Cart()
        obj.quantity=q
        obj.PRODUCT_id=pid
        obj.USER=User.objects.get(LOGIN=lid)
        obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
        obj.save()
        return JsonResponse({"status":"ok"})


def and_cart_cancel(request):
    cid=request.POST['cid']
    Cart.objects.filter(id=cid).delete()
    return JsonResponse({"status":"ok"})

def and_view_profile(request):
    lid  = request.POST['lid']
    data = User.objects.get(LOGIN=lid)
    return JsonResponse({"status":"ok","username":data.username,"gender":data.gender,"email":data.email,"phone":data.phone,"place":data.place,"post":data.post,"pin":data.pin})


def and_update_profile(request):
    lid=request.POST['lid']
    name=request.POST['name']
    gender=request.POST['gender']
    phone=request.POST['phone']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    User.objects.filter(LOGIN=lid).update(
        username = name,
        gender=gender,
        phone=phone,
        place=place,
        post=post,
        pin=pin,
    )
    return JsonResponse({'status': 'ok'})









def and_view_previous_orders(request):
    lid=request.POST['lid']
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    da=Ordersub.objects.filter(ORDER__USER__LOGIN=lid,ORDER__date__lte=date)
    if da.exists:
        ary=[]
        amt=0

        for i in da:
            amunt=int(i.quantity)*int(i.PRODUCT.price)
            ary.append({
                "id":i.id,
                "pn":i.PRODUCT.itemname,
                "prc":i.PRODUCT.price,
                "qn":i.quantity,
                "pic":i.PRODUCT.image,
                "tot":amunt,
                "ps":i.ORDER.paymentstatus,
                "shn":i.PRODUCT.SHOP.shopname+"\n"+str(i.PRODUCT.SHOP.contactno)
            })


    return JsonResponse({"status":"ok","data":ary})













def  offline_payment(request):
    lid=request.POST['lid']
    shoplist=[]
    qry=Cart.objects.filter(USER__LOGIN=lid)
    for i in qry:
        if i not in shoplist:
            shoplist.append(i.PRODUCT.SHOP.id)

    for k in shoplist:
        qry1=Order.objects.filter(SHOP=k,USER__LOGIN=lid,status="pending")
        if qry1.exists():
            qry2 = Cart.objects.filter(USER__LOGIN=lid, PRODUCT__SHOP__LOGIN=k)
            for j in qry2:
                obj1 = Ordersub()
                obj1.quantity = j.quantity
                obj1.PRODUCT_id = j.PRODUCT.id
                obj1.ORDER_id = qry[0].id
                obj1.save()

        else:
            obj=Order()
            obj.SHOP_id=str(k)
            obj.status="pending"
            obj.paymentdate="pending"
            obj.paymentstatus="pending"
            obj.date=datetime.datetime.now().date()
            obj.USER=User.objects.get(LOGIN=lid)
            obj.save()
            qry2=Cart.objects.filter(USER__LOGIN=lid,PRODUCT__SHOP=k)
            for j in qry2:
                obj1=Ordersub()
                obj1.quantity=j.quantity
                obj1.PRODUCT_id=j.PRODUCT.id
                obj1.ORDER=obj
                obj1.save()
    orderidlist=[]
    for d in shoplist:
        q=Cart.objects.filter(PRODUCT__SHOP=d,USER__LOGIN=lid)
        cartlength=len(q)
        k=Ordersub.objects.filter(ORDER__SHOP=d,ORDER__USER__LOGIN=lid,ORDER__status="pending")
        if k.exists():
            oprductlength = len(k)

            if cartlength == oprductlength:
                if k[0].id not in orderidlist:
                     orderidlist.append(k[0].ORDER.id)
                print(cartlength,oprductlength)
    print(orderidlist)
    for n in orderidlist:
            print("mmmmmmmm",n)
            Order.objects.filter(id=n).update(status="payment",paymentstatus="offline",paymentdate=datetime.datetime.now().date())
    Cart.objects.filter(USER__LOGIN=lid).delete()
    return JsonResponse({"status":"ok"})

def  online_payment(request):
    lid=request.POST['lid']
    shoplist=[]
    qry=Cart.objects.filter(USER__LOGIN=lid)
    for i in qry:
        if i not in shoplist:
            shoplist.append(i.PRODUCT.SHOP.id)

    for k in shoplist:
        qry1=Order.objects.filter(SHOP=k,USER__LOGIN=lid,status="pending")
        if qry1.exists():
            qry2 = Cart.objects.filter(USER__LOGIN=lid, PRODUCT__SHOP__LOGIN=k)
            for j in qry2:
                obj1 = Ordersub()
                obj1.quantity = j.quantity
                obj1.PRODUCT_id = j.PRODUCT.id
                obj1.ORDER_id = qry[0].id
                obj1.save()

        else:
            obj=Order()
            obj.SHOP_id=str(k)
            obj.status="pending"
            obj.paymentdate="pending"
            obj.paymentstatus="pending"
            obj.date=datetime.datetime.now().date()
            obj.USER=User.objects.get(LOGIN=lid)
            obj.save()
            qry2=Cart.objects.filter(USER__LOGIN=lid,PRODUCT__SHOP=k)
            for j in qry2:
                obj1=Ordersub()
                obj1.quantity=j.quantity
                obj1.PRODUCT_id=j.PRODUCT.id
                obj1.ORDER=obj
                obj1.save()
    orderidlist=[]
    for d in shoplist:
        q=Cart.objects.filter(PRODUCT__SHOP=d,USER__LOGIN=lid)
        cartlength=len(q)
        k=Ordersub.objects.filter(ORDER__SHOP=d,ORDER__USER__LOGIN=lid,ORDER__status="pending")
        if k.exists():
            oprductlength = len(k)

            if cartlength == oprductlength:
                if k[0].id not in orderidlist:
                     orderidlist.append(k[0].ORDER.id)
                print(cartlength,oprductlength)
    print(orderidlist)
    for n in orderidlist:
            print("mmmmmmmm",n)
            Order.objects.filter(id=n).update(status="payment",paymentstatus="online",paymentdate=datetime.datetime.now().date())
    Cart.objects.filter(USER__LOGIN=lid).delete()

    return JsonResponse({"status":"ok"})



def and_forgot_password(request):

    email=request.POST['email']
    import smtplib

    log=Login.objects.filter(username=email)
    if log.exists():
        # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # s.starttls()
        # s.login("projectfitwell@gmail.com", "ukgj crsc ohdr hlrk")
        # msg = MIMEMultipart()  # create a message.........."
        # msg['From'] = "projectfitwell@gmail.com"
        # msg['To'] = str(log[0].username)
        # msg['Subject'] = "Login Credentials for FITWELL Website!"
        # body = "Your Password is:- - " + str(log[0].password)+"\n" + "your username is:- -" + str(log[0].username)
        # msg.attach(MIMEText(body, 'plain'))
        # s.send_message(msg)
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "no"})


def and_change_password(request):
    lid = request.POST['lid']
    npw = request.POST['npw']
    cpw = request.POST['cpw']
    res = Login.objects.filter(id=lid, password=cpw)
    if res.exists():
        Login.objects.filter(id=lid).update(password=npw)
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "no"})