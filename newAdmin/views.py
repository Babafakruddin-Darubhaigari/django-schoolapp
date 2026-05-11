from django.shortcuts import render, redirect
    
from newAdmin.models import Student


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def addAdmission(request):

    # SAVE DATA
    if request.method == "POST":

        studentName = request.POST.get('name')
        studentAge = request.POST.get('age')
        studentGrade = request.POST.get('grade')

        # Store into database
        Student.objects.create(
            name = studentName,
            age = studentAge,
            grade = studentGrade
        )

        return redirect('/Ad/newAdm/')


    # FETCH DATA
    students = Student.objects.all()

    values = {
        'allStudents': students
    }

    return render(request, 'admissions/add-admission.html', values)

def admissionReport(request):
    return render(request, 'admissions/add-report.html')