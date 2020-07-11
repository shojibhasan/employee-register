

from django import forms


from .models import Employee
from django.contrib import messages
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels={
            'fullname':'Full Name',
            'emp_code':'Employee Code'
        }

    def __init__(self,*arg,**kwargs):
        super(EmployeeForm,self).__init__(*arg,**kwargs)
        self.fields['position'].empty_label ="Select"


        self.fields['emp_code'].required = False