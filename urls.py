"""rationmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('login/', views.login),
    path('login_post/', views.login_post),
    path('changepassword_adm/',views.changepassword_adm),
    path('changepassword_adm_post/',views.changepassword_adm_post),
    path('viewshopkeeper/', views.viewshopkeeper),
    path('viewshopkeeper_post/', views.viewshopkeeper_post),
    path('viewcardholder/', views.viewcardholder),
    path('viewcardholder_post/', views.viewcardholder_post),
    path('adminviewstkrequest/',views.adminviewstkrequest),
    path('adminviewapprovedstkrequest/', views.adminviewapprovedstkrequest),
    path('approverequest/<id>',views.approverequest),

    path('addstockdetails/', views.addstockdetails),
    path('addstockdetails_post/', views.addstockdetails_post),
    path('user_payment_single/', views.user_payment_single),

    path('editstockdetails/<id>', views.editstockdetails),
    path('editstockdetails_post/', views.editstockdetails_post),

    path('viewstock/', views.viewstock),
    path('viewstock_post/', views.viewstock_post),
    path('viewcomplaint/', views.viewcomplaint),
    path('viewcomplaint_post/', views.viewcomplaint_post),
    path('addreply/<id>', views.addreply),
    path('addreply_post/', views.addreply_post),
    path('addsubsidy/', views.addsubsidy),
    path('addsubsidy_post/', views.addsubsidy_post),
    path('viewsubsidy_adm/', views.viewsubsidy_adm),
    path('viewsubsidy_adm_post/', views.viewsubsidy_adm_post),
    path('approvech/<id>', views.approvech),
    path('rejectch/<id>',views.rejectch),
    path('viewcardholder_accepted/',views.viewcardholder_accepted),
    path('viewcardholder_accepted_post/',views.viewcardholder_accepted_post),
    path('viewcardholder_rejected/',views.viewcardholder_rejected),
    path('viewcardholder_rejected_post/',views.viewcardholder_rejected_post),
    path('admin_viewbooking/',views.admin_viewbooking),
    path('admin_viewbooking_post/',views.admin_viewbooking_post),
    path('adm_viewbooking_sub/<id>',views.adm_viewbooking_sub),
    path('logout/',views.logout),



    #################################################


    path('register_shop/', views.register_shop),
    path('register_shop_post/', views.register_shop_post),
    path('changepassword_shop/', views.changepassword_shop),
    path('changepassword_shop_post/', views.changepassword_adm_post),
    path('viewstockavailable/',views.viewstockavailability),
    path('sksendrqst/<id>', views.sksendrqst),
    path('sksendrqst_post/', views.sksendrqst_post),
    path('skviewapprovedstkrequest/',views.skviewapprovedstkrequest),
    path('skviewapprovedstkrequest_search/',views.skviewapprovedstkrequest_search),
    path('updatestock/', views.update_stock),
    path('updatestock_post/', views.updatestock_post),
    path('addtoken/', views.addtoken),
    path('addtoken_post/', views.addtoken_post),
    path('viewtoken/', views.viewtoken),
    path('viewtoken_post/', views.viewtoken_post),
    path('viewtokenrequest/<id>', views.viewtokenrequest),
    path('viewtokenrequest_post/', views.viewtokenrequest_post),
    path('skviewstockavailability/', views.skviewstockavailability),
    path('viewbooking/', views.viewbooking),
    path('viewbooking_post/', views.viewbooking_post),
    path('viewpayment/', views.viewpayment),
    path('viewpayment_post/', views.viewpayment_post),
    path('viewsubsidy_shop/', views.viewsubsidy_shop),
    path('viewsubsidy_shop_post/', views.viewsubsidy_shop_post),
    path('homeadmin/', views.homeadmin),
    path('homeshop/', views.homeshop),
    path('adminviewapprovedstkrequest_search/', views.adminviewapprovedstkrequest_search),
    path('adminviewstkrequest_search/', views.adminviewstkrequest_search),

    path('shomeindex1/', views.shomeindex1),

    path('viewapprovedshopkeeper/',views.viewapprovedshopkeeper),
    path('viewapprovedshopkeeper_post/',views.viewapprovedshopkeeper_post),
    path('viewrejectedshopkeeper/',views.viewrejectedshopkeeper),
    path('viewrejectedshopkeeper_post/',views.viewrejectedshopkeeper_post),
    path('approvesk/<id>',views.approvesk),
    path('rejectsk/<id>', views.rejectsk),
    path('viewbooking_sub/<id>', views.viewbooking_sub),
    path('viewupdatedstock/', views.viewupdatedstock),
    path('other_viewbooking/', views.other_viewbooking),
    path('other_viewbooking_post/', views.other_viewbooking_post),
    path('other_viewbooking_sub/<id>', views.other_viewbooking_sub),

    ############################################################user

    path('userlogin/',views.userlogin),
    path('userreg/', views.userreg),
    path('viewshop/',views.viewshop),
    path('userviewstock/', views.viewstock),
    path('viewsubsidy/',views.viewsubsidy),
    path('bookitem/', views.bookitem),
    path('makepayment/', views.makepayment),
    # path('viewbill/', views.viewbill),
    path('selecttoken/', views.selecttoken),
    path('viewstatus/', views.viewstatus),
    path('addcomplaint/', views.addcomplaint),
    path('viewreply/', views.viewreply),
    path('viewprofile/', views.viewprofile),
    path('editpro/', views.editpro),
    path('userviewupdatedstock/', views.userviewupdatedstock),
    path('addtocart/',views.addtocart),
    path('viewcart/',views.viewcart),
    path('dltfromcart/',views.dltfromcart),
    path('user_payment_/',views.user_payment_),
    path('viewprofile/', views.viewprofile),
    path('shopviewprofile/',views.shopviewprofile),
    path('editprofileshop/',views.editprofileshop),
    path('editprofileshop_post/',views.editprofileshop_post),
    path('userviewtoken/',views.userviewtoken),
    path('userchoosetoken/',views.userchoosetoken),
    path('viewshop_search/',views.viewshop_search),
    path('user_viewbooking/',views.user_viewbooking),
    path('user_viewbooking_sub/',views.user_viewbooking_sub),
    path('user_viewpayment/',views.user_viewpayment),
    path('user_token/',views.user_token),
    path('canceltoken/',views.canceltoken),


]
