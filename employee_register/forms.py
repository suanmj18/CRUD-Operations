from django import forms
from .models import Employee
class Employeeform(forms.ModelForm):

    class Meta:
        model= Employee
        fields ="__all__" #{'fullname','emp_code','mobile','position'}
        labels={
            'fullname': 'Full Name',
            'emp_code': 'Employee Code',
            'mobile': 'Mobile NUmber',
        }

    def __init__(self, *args, **kwargs):
        super(Employeeform,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required= False #for the input which is not nessary and want to leave empty