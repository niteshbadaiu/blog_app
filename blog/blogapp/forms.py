from django import forms
from blogapp.models import Student
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
# from blogapp.forms import StudentFormClass,StudentModelFormsClass,UserRegister

# django form
class StudentFormClass(forms.Form):
    name=forms.CharField()
    rno=forms.IntegerField()
    percent=forms.FloatField()


# model forms
class StudentModelFormsClass(forms.ModelForm):
    name=forms.CharField()
    rno=forms.IntegerField()
    percent=forms.FloatField()

    class Meta:
        model=Student
        fields=["name","rno","percent"]

#user register form
class UserRegister(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","first_name","last_name"]