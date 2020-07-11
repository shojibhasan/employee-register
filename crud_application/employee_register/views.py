from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    context ={'employee_list':Employee.objects.all()}
    return render(request,'employee_register/employee_list.html',context)

def employee_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        context={
            'form' : form,
        }
        return render(request, 'employee_register/employee_form.html',context)

    else:
        if id==0:

            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')