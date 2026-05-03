from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feeCollection(request):
    return HttpResponse("This is the fee collection page.")

def feeDuesReport(request):
    return HttpResponse("This is the fee dues report page.")

def feeCollectionReport(request):
    return HttpResponse("This is the fee collection report page.")