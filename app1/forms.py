from django import forms
from app1.models import *
class StudentForm(forms.ModelForm):
    class Meta:
        models=Student
        fields='__all__'