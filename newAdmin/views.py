from django.shortcuts import render
    
from newAdmin.models import Student


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def addAdmission(request):
    # Fetch all student records from the database
    students = Student.objects.all()  
    values = {'allStudents': students}
    return render(request, 'admissions/add-admission.html', values)

def admissionReport(request):
    return render(request, 'admissions/add-report.html')