from django import forms

class EmailMe(forms.Form):
    Name=forms.CharField(max_length=50)
    email=forms.EmailField()
    to=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)