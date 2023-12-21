"""
URL configuration for Thyroidproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from adminapp import views as adminapp_views
from mainapp import views as mainapp_views
from userapp import views as userapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    path('admin-dashboard',adminapp_views.admin_dashboard,name='admin_dashboard'),
    path('admin-pendings',adminapp_views.admin_pendings,name='admin_pendings'),
    path('admin-allusers',adminapp_views.admin_allusers,name='admin_allusers'),
    path('admin-upload',adminapp_views.admin_upload,name='admin_upload'),
    path('delete-dataset/<int:id>',adminapp_views.delete_dataset, name = 'delete_dataset'),
    path('admin-view',adminapp_views.admin_view,name='admin_view'),
    path('accept-user/<int:id>', adminapp_views.accept_user, name = 'accept_user'),
    path('reject-user/<int:id>', adminapp_views.reject_user, name = 'reject'),
    path('delete-user/<int:id>', adminapp_views.delete_user, name = 'delete_user'),
    path('admin-Xg_algo',adminapp_views.admin_Xg_algo,name='admin_Xg_algo'),
    path('admin-ada_algo',adminapp_views.admin_ada_algo,name='admin_ada_algo'),
    path('admin-Logistic-algo',adminapp_views.admin_Logistic_algo,name='admin_Logistic_algo'),
    path('admin-knn-algo',adminapp_views.admin_knn_algo,name='admin_knn_algo'),
    path('admin-Randomforest-algo',adminapp_views.admin_Randomforest_algo,name='admin_Randomforest_algo'),
    path('admin-greadient-algo',adminapp_views.admin_greadient_algo,name='admin_greadient_algo'),
    path('admin-svm-algo',adminapp_views.admin_svm_algo,name='admin_svm_algo'),
    path('admin-dt-algo',adminapp_views.admin_dt_algo,name='admin_dt_algo'),
    path('XGBOOST_btn', adminapp_views.XGBOOST_btn, name='XGBOOST_btn'),
    path('ADABoost_btn', adminapp_views.ADABoost_btn, name='ADABoost_btn'),
    path('KNN_btn', adminapp_views.KNN_btn, name='KNN_btn'),
    path('GR_btn', adminapp_views.GR_btn, name='GR_btn'),
    path('logistic_btn', adminapp_views.logistic_btn, name='logistic_btn'),
    path('randomforest_btn', adminapp_views.randomforest_btn, name='randomforest_btn'),
    path('SVM_btn', adminapp_views.SVM_btn, name='SVM_btn'),
    path('Decisiontree_btn', adminapp_views.Decisiontree_btn, name='Decisiontree_btn'),
    path('admin-graph',adminapp_views.admin_graph,name='admin_graph'),
    path('admin-feedback',adminapp_views.admin_feedback,name='admin_feedback'),
    path('admin-sentiment',adminapp_views.admin_sentiment,name='admin_sentiment'),
    path('admin-feedbackgraph',adminapp_views.admin_feedbackgraph,name='admin_feedbackgraph'),
    path('admin-logout', adminapp_views.admin_logout, name='admin_logout'),
    path('admin-view',adminapp_views.admin_view,name='admin_view'),
    path('view_view', adminapp_views.view_view, name='view_view'),
    
    #main
    path('',mainapp_views.main_homepage,name='main_homepage'),
    path('aboutus',mainapp_views.aboutus,name='aboutus'),
    path('contact',mainapp_views.contact,name='contact'),
    path('user-login',mainapp_views.user_login,name='user_login'),
    path('admin-login',mainapp_views.admin_login,name='admin_login'),
    path('register',mainapp_views.register,name='register'),
    path('otp',mainapp_views.otp,name='otp'),
    path('forgotpwd',mainapp_views.forgotpwd,name='forgotpwd'),
    
    
    #user
    path('user-dashboard',userapp_views.user_dashboard,name='user_dashboard'),
    path('user-profile',userapp_views.user_profile,name='user_profile'),
    path('user-feedback',userapp_views.user_feedback,name='user_feedback'),
    path('user-predict',userapp_views.user_predict,name='user_predict'),
    path('user-result',userapp_views.user_result,name='user_result'),
    path('userlogout', userapp_views.userlogout, name = 'userlogout'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
