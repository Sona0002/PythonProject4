from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Mobile
from . forms import MobileForm

# Create your views here.
def index(request):
    mobile=Mobile.objects.all()
    context={
        'mobile_list':mobile
    }

    return render(request,'index.html',context)

def detail(request,mobile_id):
    mobile=Mobile.objects.get(id=mobile_id)
    return render(request,"detail.html",{'mobile':mobile})

def add_mobile(request):
    if request.method=="POST":
        model_name = request.POST.get('model_name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        mobile=Mobile(model_name=model_name,desc=desc,price=price,img=img)
        mobile.save()

    return render(request,'add.html')

def update(request,id):
    mobile=Mobile.objects.get(id=id)
    form=MobileForm(request.POST or None, request.FILES, instance=mobile)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'mobile':mobile})

def delete(request,id):
    if request.method=="POST":
        mobile=Mobile.objects.get(id=id)
        mobile.delete()
        return redirect('/')
    return render(request,'delete.html')
