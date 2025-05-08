from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self, *args, **kkwargs):
        super(EmployeeForm, self).__init__(*args, **kkwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False