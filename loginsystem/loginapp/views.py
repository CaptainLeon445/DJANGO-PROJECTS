
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from jupyterlab_server import slugify
from .models import SavePassword
from .forms import  SignUp,LoginForm,Svepassword
from django.conf import settings

# Create your views here.

def create_account(request):
    if request.method=='POST':
        user_form=SignUp(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request, 'loginapp/created.html', {'new_user':new_user})
           
    else:
        user_form=SignUp()
    return render(request, 'loginapp/create.html', {'user_form': user_form})

def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Authenticated Successfully!')
            else:
                return HttpResponse('Invalid Login')
    else:
        form=LoginForm()
    return render(request,'loginapp/login.html',{'form':form})


     

@login_required
def welcome(request):
    return render(request, 'loginapp/welcome.html', {'greeting':'welcome'})

@login_required
def create_pwd(request):
    if request.method=='POST':
        form = Svepassword(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=request.user
             
            slug=slugify(cd['title'])
           
            savepassword=SavePassword.objects.create(user=user,title=cd['title'],password=cd['password'],slug=slug)
            savepassword.save()
            
            return redirect('loginapp:pwd_list')
            

    else:
        form=Svepassword()
    return render(request,'loginapp/createpwd.html',{'form':form})
    

@login_required
def pwd_list(request):
    passwords=SavePassword.objects.all().order_by('-id')
   
    return render(request, 'loginapp/pwd_list.html', {'passwords':passwords})

@login_required
def pwd_detail(request,year,day,month,pwd,id):
    pwd=get_object_or_404(SavePassword,created__year=year,created__day=day,created__month=month,slug=pwd,id=id)
    return render(request, 'loginapp/pwd_details.html', {'pwd':pwd})

@login_required
def delete(request,id):
    delete=SavePassword.objects.get(id=id).delete()
    delete
    return redirect('loginapp:pwd_list')

@login_required
def Edit(request,id):
    new=SavePassword.objects.get(id=id)
    if request.method=='POST':
        form = Svepassword(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=request.user
            
            slug=slugify(cd['title'])

            new.title=cd['title']
            new.password=cd['password']
            new.slug=slug
            new.save()
            return redirect('loginapp:pwd_list')
            

    else:
        
        form=Svepassword(instance=[title,password])
    return render(request,'loginapp/edit.html',{'form':form,'idl':new})
    
    #return redirect('loginapp:pwd_list')