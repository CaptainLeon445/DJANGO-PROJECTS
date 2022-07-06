
from django.shortcuts import render
from .forms import EmailMe
from django.core import mail

# Create your views here.

def SendEmail(request):
    
    if request.method=="POST":
        form=EmailMe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject = cd['Name']
            message = cd['message']
            with mail.get_connection() as connection:
                mail.EmailMessage(
                    subject, message, [cd['email']], [cd['to']],
                    connection=connection,
                ).send()
            
            return render(request,"sent.html")
            


    else:
        form=EmailMe()
    return render(request, 'sendemail.html', {'form':form})
