from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForms):
    class Meta:
        model = Teacher
        fields = ['regid', 'name', 'dept']
        labels = {"regid": "20000XXXX", "name": "Enter name", "dept": "CSE or ECE"}
