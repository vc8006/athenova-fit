from django.shortcuts import render
from .models import Image,User
from django.shortcuts import redirect

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def events(request):
    return render(request,"events.html")

def Programs(request):
    return render(request,"Programs.html")

def contact(request):
    return render(request,"contact.html")

def contactS(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        subject = request.POST.get("subject")
        message = request.POST.get('message')
        date = request.POST.get('date')
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        lifestyle = request.POST.get("lifestyle")
        activity = request.POST.get("activity")
        goal = request.POST.get("goal")
        frequency = request.POST.get("frequency")
        usr = User(name=name,email=email,phone=number,subject=subject,message=message,date=date,gender=gender,age=age,lifestyle=lifestyle,activity_level=activity,goal=goal,frequency=frequency)
        try:
            usr.save()
            return redirect(contact)
        except Exception as e:
            print(e)
            return redirect(contact)
    return render(request,"contact.html")

def homeS(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        lifestyle = request.POST.get("lifestyle")
        activity = request.POST.get("activity")
        goal = request.POST.get("goal")
        frequency = request.POST.get("frequency")
        usr = User(name=name,email=email,phone=number,gender=gender,age=age,lifestyle=lifestyle,activity_level=activity,goal=goal,frequency=frequency)
        try:
            usr.save()
            return redirect(home)
        except Exception as e:
            print(e)
            return redirect(home)
    return render(request,"index.html")

def gallery(request):
    img = Image.objects.all()
    return render(request,'gallery.html',{'img':img})