from django import forms
from django.contrib.auth.models import User



class SignUp(forms.ModelForm):
    Lname=forms.CharField(label='Last Name',max_length=20)
    Pnumber=forms.IntegerField(label="Phone Number")
    #DOB=forms.DateField()
    password=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput) 

    class Meta:
        model= User
        fields= ('username', 'first_name', 'email')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password don\'t match")
        return cd['password2']


   

class LoginForm(forms.Form):
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password", widget=forms.PasswordInput)

class Svepassword(forms.Form):
    title=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)
    

    def __str__(self):
        return self.title


