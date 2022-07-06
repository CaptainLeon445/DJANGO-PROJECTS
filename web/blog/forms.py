from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

class sharepost(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(required=False,widget=forms.Textarea)