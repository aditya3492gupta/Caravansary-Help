# from msilib.schema import SelfReg
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from login.models import food_enquiry
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
    return render(request, 'contact_us.html')

def food_request(request):
    
    return render(request,'food_request.html')

def home(request):
    return render(request, 'home.html')

def laundary_page(request):
    return render(request, 'laundary_page.html')

def leave(request):
    return render(request, 'leave.html')

def mess(request):
    return render(request, 'mess.html')

def photos(request):
    return render(request, 'photos.html')

def services(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        room=request.POST.get('room')
        message=request.POST.get('message')
        # reason=request.POST.get('reason')
        # print(name,email,room,message)
        ser=services(name=name,email=email,room=room,message=message)
        ser.save()
        print("data written")
    return render(request, 'services.html')

def food_enq(request):
    if request.method=="POST":
        name=request.POST.get('name')
        day=request.POST.get('day')
        date=request.POST.get('date')
        time=request.POST.get('time')
        reason=request.POST.get('reason')
        print(name,day,date,time,reason)
        ins=food_enq(name=name,day=day,date=date,time=time,reason=reason)
        ins.save()
        print("data written")
    return render(request,'food_request.html')