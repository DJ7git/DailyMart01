from django.urls import path
from . import views

urlpatterns = [
    path('userindex',views.userindex,name="userindex"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userregistration',views.userregistration,name="userregistration"),
    path('getuserdata',views.getuserdata,name="getuserdata"),
    path('publicdata',views.publicdata,name="publicdata"),    
    path('userlogout',views.userlogout,name="userlogout"),
    path('viewcategoryastable',views.viewcategoryastable,name="viewcategoryastable"),
    path('viewproductastable',views.viewproductastable,name="viewproductastable"),
    path('viewcategoryascard',views.viewcategoryascard,name="viewcategoryascard"),
    path('viewproductascard/<str:category>',views.viewproductascard,name="viewproductascard"),
    path('productsinglepage/<int:id>',views.productsinglepage,name="productsinglepage"),
    path('addfeedback',views.addfeedback,name="addfeedback"),
    path('getfeedback',views.getfeedback,name="getfeedback"),
    path('about',views.about,name="about"),
    path('cart',views.cart,name="cart"),
    path('viewcartastable',views.viewcartastable,name="viewcartastable"),
    path('addtocart/<int:id>',views.addtocart,name="addtocart"),    
    path('checkout',views.checkout,name="checkout"),
    path('deletecartitem/<int:id>',views.deletecartitem,name="deletecartitem"),
    path('checkoutdata',views.checkoutdata,name="checkoutdata"),
    path('success',views.success,name="success"),
]