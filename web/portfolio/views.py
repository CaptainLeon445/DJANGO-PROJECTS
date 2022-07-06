from django.shortcuts import render,redirect
from .models import profile, projects
from .forms import contactForm
from django.core import mail
# Create your views here.

def index(request):
    return render(request,'portfolio/base.html')
def homepage (request):
    project=profile.objects.all()
    return render(request,'portfolio/homepage.html',{'projects':project})

def portfolio (request):
    portfolio=projects.objects.all()
    portfolio={'portfolio':portfolio}
    return render(request, "portfolio/portfolio.html", portfolio)

def sendemail(request):
    
    if request.method=="POST":
        form=contactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject = cd['subject']
            message = cd['message']
            with mail.get_connection() as connection:
                mail.EmailMessage(
                    subject, message, [cd['email']], [cd['to']],
                    connection=connection,
                ).send()
            
            
            return redirect("homepage")
            


    else:
        form=contactForm()
    return render(request, 'portfolio/contact.html', {'form':form})
