from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def index(request):
    try:
        if 'q' in request.GET:
            q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(email__icontains=q))
        data = Student.objects.filter(multiple_q) 
        if not data:
            messages.warning(request,"No data found")
        else:
            pass
    except:
        pass
        data=Student.objects.all()
    page=Paginator(data,10)
    page_list=request.GET.get('page')
    page=page.get_page(page_list)
    context={'page':page}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


def insertedData(request):
   
    if request.method=="POST":
        RollNumber=request.POST.get('roll')
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Age=request.POST.get('age')
        Gender=request.POST.get('gender')
        Artist=request.POST.get('artist')
    try:
        if Student.objects.get(email=Email):
            messages.warning(request,"Email is Already Taken")
            return redirect("/")
    except:
        pass
        query=Student(rollnumber=RollNumber,name=Name,email=Email,age=Age,gender=Gender)
    messages.success(request,'Student Details Added Successfully')
    query.save()
    return redirect("/")
    return render(request,'index.html')
    

def update(request,id):
    if request.method=="POST":
        RollNumber=request.POST['roll']
        Name=request.POST['name']
        Email=request.POST['email']
        Age=request.POST['age']
        Gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.rollnumber=RollNumber
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
   
