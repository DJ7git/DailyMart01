from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from userapp.models import *

# Create your views here.

def defaultadmin(request):
    return HttpResponse('Hello World from Admin App page')

def aindex(request):
    categorycount1 = Category.objects.all().count()
    productcount1 = Product.objects.all().count()
    registeredusercount1 = userdata.objects.all().count()
    feedbackcount1 = feedbackdata.objects.all().count()
    ordercount1 = Checkout.objects.all().count()
    return render(request, 'aindex.html',{'categorycount':categorycount1,'productcount':productcount1,'registeredusercount':registeredusercount1,'feedbackcount':feedbackcount1,'ordercount':ordercount1})


def addcategory(request):
    return render(request,'addcategory.html')

def getcategory(request):
    if request.method == 'POST':
        categoryname1 = request.POST['categoryname']
        categoryimage1 = request.FILES['categoryimage']
        data = Category(categoryname=categoryname1,categoryimage=categoryimage1)
        data.save()
    return redirect('aindex')

def viewcategoryastable(request):
    data1 = Category.objects.all()

    return render(request,'viewcategoryastable.html',{'categorydatainDB':data1})


def getproduct(request):
    if request.method == 'POST':
        productname1 = request.POST['productname']
        productimage1 = request.FILES['productimage']
        productprice1 = request.POST['productprice']
        productcategory1 = request.POST['productcategory']
        productdescription1 = request.POST['productdescription']
        data = Product(productname=productname1,productimage=productimage1,productprice=productprice1,productcategory=productcategory1,productdescription=productdescription1)
        data.save()
    return redirect('aindex')

def viewproductastable(request):
    data = Product.objects.all()
    return render(request,'viewproductastable.html',{'productdatainDB':data})

def editcategory(request,id):
    data = Category.objects.filter(id=id)
    return render(request,'editcategory.html',{'categorydatafromDBtobeedited':data})

def updatecategory(request,id):
    if request.method == 'POST':
        categoryname1 = request.POST['categoryname']
        try:
            img_c = request.FILES['categoryimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).categoryimage
        Category.objects.filter(id=id).update(categoryname=categoryname1,categoryimage=file)
    return redirect('viewcategoryastable')

def deletecategory(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('viewcategoryastable')

def editproduct(request,id):
    data = Product.objects.filter(id=id)
    data2 = Category.objects.all()
    return render(request,'editproduct.html',{'productfromDBtobeedited':data, 'categorydatainDB':data2})

def addproduct(request):
    data = Category.objects.all()
    return render(request,'addproduct.html',{'categorydatainDB':data})    


def updateproduct(request,id):
    if request.method == 'POST':
        productname1 = request.POST['productname']
        productprice1 = request.POST['productprice']
        productcategory1 = request.POST['productcategory']
        productdescription1 = request.POST['productdescription']
        try:
            img_c = request.FILES['productimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).productimage
        Product.objects.filter(id=id).update(productname=productname1,productprice=productprice1,productcategory=productcategory1,productdescription=productdescription1,productimage=file)
    return redirect('viewproductastable')

def deleteproduct(request,id):
    Product.objects.filter(id=id).delete()
    return redirect('viewproductastable')

def viewregisteredusers(request):
    data = userdata.objects.all()
    return render(request,'viewregisteredusers.html',{'allregisteredusersinDB':data})

def viewfeedback(request):
    data = feedbackdata.objects.all()
    return render(request,'viewfeedback.html',{'feedbackdatainDB':data})

def vieworders(request):
    data = Checkout.objects.all()
    return render(request,'vieworders.html',{'orderdatainDB':data})