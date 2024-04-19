"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from FitWell import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('login_post', views.login_post),
    path('logout', views.logout),
    path('adminhome', views.adminhome),
    path('changepassword', views.changepassword),
    path('changepassword_post', views.changepassword_post),
    path('addtrainer', views.addtrainer),
    path('addtrainer_post', views.addtrainer_post),
    path('edittrainer/<id>', views.edittrainer),
    path('edittrainer_post/<id>', views.edittrainer_post),
    path('deletetrainer/<id>', views.deletetrainer),
    path('viewtrainer', views.viewtrainer),
    path('allocatetrainer/<id>', views.allocatetrainer),
    path('allocation_post/<id>', views.allocation_post),
    path('viewrequestfromuser', views.viewrequestfromuser),
    path('approverequest/<id>', views.approverequest),
    path('rejectrequest/<id>', views.rejectrequest),
    path('approvedrequest', views.approvedrequest),
    path('approvedshop', views.approvedshop),
    path('approveshops/<id>', views.approveshops),
    path('rejectshops/<id>', views.rejectshops),
    path('complaint', views.complaint),
    path('admin_viewrating/<id>', views.admin_viewrating),
    path('send_reply/<id>', views.send_reply),
    path('send_reply_post/<id>', views.send_reply_post),
    path('viewfeedback', views.viewfeedback),
    path('viewshops', views.viewshops),
    path('approvedshop', views.approvedshop),
    path('addbatch', views.addbatch),
    path('addbatch_post', views.addbatch_post),
    path('editbatch/<id>', views.editbatch),
    path('editbatch_post/<id>', views.editbatch_post),
    path('deletebacth/<id>', views.deletebacth),
    path('viewbatch', views.viewbatch),

    path('trainerhome',  views.trainerhome),
    path('viewtrainerprofile',  views.viewtrainerprofile),
    path('viewallocation',  views.viewallocation),
    path('viewuser/<id>',  views.viewuser),
    path('addworkout',  views.addworkout),
    path('addworkout_post',  views.addworkout_post),
    path('viewworkout',  views.viewworkout),
    # path('viewexercise',  views.viewexercise),

    path('viewexercise/<id>', views.viewexercise),
    path('editworkout/<id>',  views.editworkout),
    path('editworkout_post/<id>',  views.editworkout_post),
    path('deleteworkout/<id>',  views.deleteworkout),
    path('uploadmealplans',  views.uploadmealplans),
    path('uploadmealplans_post',  views.uploadmealplans_post),
    path('viewmealplans',  views.viewmealplans),
    path('editmealplans/<id>',  views.editmealplans),
    path('editmealplans_post/<id>',  views.editmealplans_post),
    path('deletemealplans/<id>',  views.deletemealplans),
    path('addtips/<id>',  views.addtips),
    path('addtips_post/<id>',  views.addtips_post),
    path('edittips/<id>',  views.edittips),
    path('edittips_post/<id>',  views.edittips_post),
    path('deletetips/<id>',  views.deletetips),
    path('viewtips/<id>',views.viewtips),
    path('viewrating',  views.viewrating),
    path('edittrainerprofile/<id>',  views.edittrainerprofile),
    path('edittrainerprofile_post/<id>',  views.edittrainerprofile_post),
    path('trainer_changepassword',  views.trainer_changepassword),
    path('trainer_changepassword_post',  views.trainer_changepassword_post),



    path('shophome', views.shophome),
    path('viewshopprofile', views.viewshopprofile),
    path('editshopprofile/<id>', views.editshopprofile),
    path('editshopprofile_post/<id>',  views.editshopprofile_post),
    path('registration', views.registration),
    path('registration_post', views.registration_post),
    path('addproduct', views.addproduct),
    path('addproduct_post', views.addproduct_post),
    path('viewproducts', views.viewproducts),
    path('editproducts/<id>', views.editproducts),
    path('editproducts_post/<id>',  views.editproducts_post),
    path('deleteproduct/<id>', views.deleteproduct),
    path('orderrequest', views.orderrequest),
    path('approveorder/<id>', views.approveorder),
    path('rejectorder/<id>', views.rejectorder),
    path('vieworder/<id>', views.vieworder),
    path('viewapprovedorder', views.viewapprovedorder),
    # path('viewproduct/<id>', views.viewproduct),
    path('viewpayment', views.viewpayment),
    path('viewpaymentdetails/<id>', views.viewpaymentdetails),

    path('and_login',views.and_login),
    path('and_user_register',views.and_user_register),
    path('and_view_products',views.and_view_products),
    path('and_user_send_request',views.and_user_send_request),
    path('and_view_request_status',views.and_view_request_status),
    path('and_view_reply',views.and_view_reply),
    path('and_view_shops',views.and_view_shops),
    path('and_view_tips',views.and_view_tips),
    path('and_view_meal_plans',views.and_view_meal_plans),
    path('and_add_health_details',views.and_add_health_details),
    path('and_view_cart',views.and_view_cart),
    path('and_view_batch',views.and_view_batch),
    path('and_view_workouts',views.and_view_workouts),
    path('and_view_trainer',views.and_view_trainer),
    path('and_send_feedback',views.send_feedback),
    path('and_send_complaints',views.and_send_complaints),
    path('and_send_rating',views.and_send_rating),
    path('add_to_cart',views.add_to_cart),
    path('and_cart_cancel',views.and_cart_cancel),
    path('and_view_profile',views.and_view_profile),
    path('and_view_added_health',views.and_view_added_health),
    path('offline_payment',views.offline_payment),
    path('online_payment',views.online_payment),
    path('viewpaymenthistory',views.viewpaymenthistory),
    path('and_forgot_password',views.and_forgot_password),
    path('and_view_previous_orders',views.and_view_previous_orders),
    path('and_update_profile',views.and_update_profile),


    path('add_chat',views.add_chat),
    path('view_chat',views.view_chat),
    path('chatt/<u>',views.chatt),
    path('chatsnd/<u>',views.chatsnd),
    path('chatrply',views.chatrply),
    path('and_change_password',views.and_change_password),

]
