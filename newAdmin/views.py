from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def addAdmission(request):
    values = {"name": "Baba", "age": 25, "grade": "10th"}
    return render(request, 'admissions/add-admission.html', values)

def admissionReport(request):
    return render(request, 'admissions/add-report.html')