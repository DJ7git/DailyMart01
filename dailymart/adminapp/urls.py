from django.urls import path
from . import views

urlpatterns = [
    path('',views.aindex,name="aindex"),
    path('addcategory',views.addcategory,name="addcategory"),
    path('getcategory',views.getcategory,name="getcategory"),
    path('viewcategoryastable',views.viewcategoryastable,name="viewcategoryastable"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('getproduct',views.getproduct,name="getproduct"),
    path('viewproductastable',views.viewproductastable,name="viewproductastable"),
    path('editcategory/<int:id>',views.editcategory,name="editcategory"),
    path('updatecategory/<int:id>',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:id>',views.deletecategory,name="deletecategory"),        
    path('editproduct/<int:id>',views.editproduct,name="editproduct"),
    path('updateproduct/<int:id>',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:id>',views.deleteproduct,name="deleteproduct"),
    path('viewregisteredusers',views.viewregisteredusers,name="viewregisteredusers"),
    path('viewfeedback',views.viewfeedback,name="viewfeedback"),
    path('vieworders',views.vieworders,name="vieworders"),    
]