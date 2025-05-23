from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import get_object_or_404

# Create your views here.

def employee_list(request):
    context = {'employee_list' : Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request, id):

    # Ensure the employee exists before attempting deletion
    employee = get_object_or_404(Employee,pk=id)
    
   # Log the ID being deleted
    print(f"Deleting Employee with ID: {employee.id}")
    
    # employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')