from django.shortcuts import render


# Create your views here.
def addAdmission(request):
    return render(request, 'admissions/add-admission.html')

def admissionReport(request):
    return render(request, 'admissions/admission-report.html')