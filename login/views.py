# from msilib.schema import SelfReg
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from login.models import Food_request,Services,Leave,Contact,Laundry
# Create your views here.
# adity@3492guptA
def index_(request):
    if request.user.is_anonymous:
        # print(request.user)
        return redirect("/logins")
    return render(request,'dashboard.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        # print(username,password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            return render(request,'index.html')
        # No backend authenticated the credentials
    return render(request,'index.html') 

def logoutUser(request):
    logout(request)
    return redirect("/logins")

def contact_us(request):
    if request.method=="POST":
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        con=Contact(fname=fname,lname=lname,email=email,phone=phone,message=message)
        con.save()
    return render(request, 'contact_us.html')

def food_request(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        day=request.POST.get('day','')
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        reason=request.POST.get('reason','')
        # print(name,day,date,time,reason)
        ins=Food_request(name=name,day=day,date=date,time=time,reason=reason)
        ins.save()
        # print("data written")
    return render(request,'food_request.html')
    # return render(request,'food_request.html')

def home(request):
    return render(request, 'home.html')

def laundary_page(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        admn=request.POST.get('admn','')
        inputp=request.POST.get('inputp','')
        inputj=request.POST.get('inputj','')
        inputs=request.POST.get('inputs','')
        inputt=request.POST.get('inputt','')
        inputk=request.POST.get('inputk','')
        inputpy=request.POST.get('inputpy','')
        inputtp=request.POST.get('inputtp','')
        inputsho=request.POST.get('inputsho','')
        inputun=request.POST.get('inputun','')
        inputb=request.POST.get('inputb','')
        inputsp=request.POST.get('inputsp','')
        inputbs=request.POST.get('inputbs','')
        inputpc=request.POST.get('inputpc','')
        inputht=request.POST.get('inputht','')
        inputhc=request.POST.get('inputhc','')
        inputbt=request.POST.get('inputbt','')
        inputo=request.POST.get('inputo','')
        ttl=request.POST.get('ttl','')
        lnd=Laundry(name=name,admn=admn,inputp=inputp,inputj=inputj,inputs=inputs,inputt=inputt,inputk=inputk,inputpy=inputpy,inputtp=inputtp,inputsho=inputsho,inputun=inputun,inputb=inputb,inputsp=inputsp,inputbs=inputbs,inputpc=inputpc,inputht=inputht,inputhc=inputhc,inputbt=inputbt,inputo=inputo,ttl=ttl)
        lnd.save()
    return render(request, 'laundary_page.html')

def leave(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        admn=request.POST.get('admn','')
        phone=request.POST.get('phone','')
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        reason=request.POST.get('reason','')
        relate=request.POST.get('relate','')
        rphone=request.POST.get('rphone','')
        add=request.POST.get('add','')
        info=request.POST.get('info','')
        rdate=request.POST.get('rdate','')
        rtime=request.POST.get('rtime','')
        lea=Leave(name=name,admn=admn,phone=phone,date=date,time=time,reason=reason,relate=relate,rphone=rphone,add=add,info=info,rdate=rdate,rtime=rtime)
        lea.save()
    return render(request, 'leave.html')

def mess(request):
    return render(request, 'mess.html')

def photos(request):
    return render(request, 'photos.html')

def services(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        room=request.POST.get('room','')
        message=request.POST.get('message','')
        # reason=request.POST.get('reason')
        # print(name,email,room,message)
        ser=Services(name=name,email=email,room=room,message=message)
        ser.save()
        # print("data written")
    return render(request, 'services.html')

# def food_enq(request):
    