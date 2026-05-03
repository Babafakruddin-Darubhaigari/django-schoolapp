from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addAdmission(request):
    return HttpResponse("This is the add admission page.")

def admissionReport(request):
    return HttpResponse("This is the admission report page.")