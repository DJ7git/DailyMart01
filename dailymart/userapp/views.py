from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
from adminapp.models import *
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def defaultuser(request):
    return HttpResponse('Hello World from User App page')

def userindex(request):
    return render(request, 'userindex.html')

def userlogin(request):
    return render(request, 'userlogin.html')

def userregistration(request):
    return render(request, 'userregistration.html')

def productsinglepage(request,id):
    data = Product.objects.filter(id=id)
    return render(request,'productsinglepage.html',{'productdatainDB':data})

def getuserdata(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        userpassword1 = request.POST['userpassword']
        usermail1 = request.POST['usermail']
        userphone1 = request.POST['userphone']

        data = userdata(dbusername=username1,dbuserpassword=userpassword1,dbusermail=usermail1,dbuserphone=userphone1)
        data.save()
        
    return redirect("userregistration")

def publicdata(request):
    if request.method == "POST":
        username2=request.POST.get('username')
        password2=request.POST.get('userpassword')
        if userdata.objects.filter(dbusername=username2,dbuserpassword=password2).exists():
           data = userdata.objects.filter(dbusername=username2,dbuserpassword=password2).values('dbusermail','dbuserphone','id').first()
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['dbuserphone'] 
           request.session['email_u'] = data['dbusermail'] 
           request.session['username_u'] = username2
           request.session['password_u'] = password2
           return redirect('userindex')
        else:
            return render(request,'userlogin.html',{'msg':'invalid user credentials'})
    else:
        return redirect('publiclogin')
    
def userlogout(request):
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('userindex')

def viewcategoryastable(request):
    data = Category.objects.all()
    return render(request,'viewcategoryastable.html',{'categorydatainDB':data})

def viewproductastable(request):
    data = Product.objects.all()
    return render(request,'viewproductastable.html',{'productdatainDB':data})

def viewcategoryascard(request):
    data = Category.objects.all()
    return render(request,'viewcategoryascard.html',{'categorydatainDB':data})

def viewproductascard(request,category):
    if(category == 'all'):
        data = Product.objects.all()
    else:
        data = Product.objects.filter(productcategory=category)
    return render(request,'viewproductascard.html',{'productdatainDB':data})

def addfeedback(request):
    data = userdata.objects.all()
    return render(request, 'addfeedback.html',{'feedbackdatainDB':data})

def getfeedback(request):
    if request.method == 'POST':
        feedbackuser1 = request.session.get('username_u')
        feedbackmail1 = request.session.get('email_u')
        feedbackreview1 = request.POST['feedbackreview']
        data = feedbackdata(feedbackuser=feedbackuser1,feedbackmail=feedbackmail1,feedbackreview=feedbackreview1)
        data.save()
    return redirect("userindex")

def about(request):
    return render(request, 'about.html')

def cart(request):

    u_id1 = request.session.get('u_id')

    # Get cart data and total sum in one query
    cart_items = Cart.objects.filter(usercart=u_id1, status=0)
    # Calculate the total sum of the cart
    total_sum = cart_items.aggregate(total_sum=Sum('total'))['total_sum'] or 0


    # Return the rendered page with the cart data and total sum
    return render(request, 'cart.html', {'cartdatainDB': cart_items, 'total_sum': total_sum})

def checkout(request):
    
    # Retrieve user ID from the session
    u_id1 = request.session.get('u_id')


    # If the user is not logged in, redirect to login page
    if not u_id1:
        return redirect('userlogin')

    # Fetch cart items for the user that are still in the cart (status=0 means active)
    cart_items = Cart.objects.filter(usercart=u_id1, status=0)

    # If no cart items, redirect to the cart page
    if not cart_items.exists():
        messages.error(request, 'Your cart is empty. Add some products to continue.')
        return redirect('cart')

    # Calculate the total sum of the cart
    total_sum = cart_items.aggregate(total_sum=Sum('total'))['total_sum'] or 0

    return render(request,'checkout.html',{'cart_items':cart_items,'total_sum': total_sum})

def addtocart(request,id):
    if request.method == "POST":
        u_id1 = request.session.get('u_id')
        quantity1 = request.POST.get('quantity')
        total1 = request.POST.get('total')
        data = Cart(usercart=userdata.objects.get(id=u_id1),product=Product.objects.get(id=id),quantity=quantity1,total=total1)
        data.save()
    return redirect('viewcategoryascard')

def viewcartastable(request):
    data = Cart.objects.all()
    return render(request,'cart.html',{'cartdatainDB':data})

def deletecartitem(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('cart')

def checkoutdata(request):
    if request.method == "POST":
        checkoutid1 = request.session.get('u_id')
        address1 = request.POST.get('address')
        city1 = request.POST.get('city')
        pincode1 = request.POST.get('pincode')
        country1 = request.POST.get('country')

        # Fetch the user once instead of in each loop iteration
        user = userdata.objects.get(id=checkoutid1)        

        cart_items = Cart.objects.filter(usercart = checkoutid1,status = 0)

        for i in cart_items:
            # Check if checkout already exists for this user and cart item to prevent overwriting
            if not Checkout.objects.filter(usercheckout=user, usercart=i).exists():
                data = Checkout(usercheckout = user,usercart = i,address=address1,city=city1,pincode=pincode1,country=country1)
                data.save()

            # Update the cart status to 'processed' only if it's still in status 0
            i.status = 1
            i.save()

        return redirect('success')

def success(request):
    user = request.session.get('u_id')
    data = Checkout.objects.filter(usercheckout=user).order_by('id')
    return render(request,'success.html',{'orderdatainDB':data})

