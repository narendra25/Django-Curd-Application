from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    data=Student.objects.all()
    context={'data':data}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


def insertedData(request):
   
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Age=request.POST.get('age')
        Gender=request.POST.get('gender')   
    try:
        if Student.objects.get(email=Email):
            messages.warning(request,"Email is Already Taken")
            return redirect("/")
    except:
        pass
    query=Student(name=Name,email=Email,age=Age,gender=Gender)
    messages.success(request,'Student Details Added Successfully')
    query.save()
    return redirect("/")
    return render(request,'index.html')
    

def update(request,id):
    if request.method=="POST":
        Name=request.POST['name']
        Email=request.POST['email']
        Age=request.POST['age']
        Gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=Name
        edit.email=Email
        edit.age=Age
        edit.gender=Gender
        #try:
            #if Student.objects.get(email=edit.email):
                #messages.warning(request,"Already mail exists. Enter New mail")
                #return redirect("/")
        #except:
            #pass
        edit.save()
        messages.success(request,"Student Details successfully Updated..")
        return redirect("/")
    d=Student.objects.get(id=id)
    context={'d':d}
    return render(request,'about.html',context)

def delete(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.success(request,"Student Details Successfully deleted..")
    return redirect("/")
   