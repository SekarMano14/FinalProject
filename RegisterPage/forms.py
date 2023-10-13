from django import forms

# Create your models here.
from RegisterPage.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

