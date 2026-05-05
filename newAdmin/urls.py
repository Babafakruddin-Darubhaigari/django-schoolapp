from django.urls import path
#from django.contrib import admin
from newAdmin.views import addAdmission, admissionReport

urlpatterns = [
    
    path('newAdm/', addAdmission,),
    path('admReport/', admissionReport,),
]