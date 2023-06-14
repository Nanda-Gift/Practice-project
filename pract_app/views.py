from django.shortcuts import render,HttpResponse,redirect
from pract_app.models import account_profile,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import auth
import re

# Create your views here.
@login_required(login_url="signin")
def home(request):
    return render(request,'index.html')


def sign_up(request):
    
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return redirect('signup') 
        if len(password)<=5:
            messages.warning(request,"Password must be atleast 5 character")
            return redirect('signup') 
        elif not re.search("[a-z]", password):
            flag = -1
            
        elif not re.search("[A-Z]", password):
            flag = -1
            
        elif not re.search("[0-9]", password):
            flag = -1
            
        elif not re.search("[_@$#%^*()-]" , password):
            flag = -1  
        else:
            pass
        if(flag==0):
            try:
                if User.objects.get(username=email):
                
                    messages.info(request,"Email is Taken")
                    return redirect('signup') 


            except Exception as identifier:
                pass

            user_model=User.objects.get(username=username)
            profile=account_profile.objects.create(user=user_model,id_user=user_model.id)
            profile.save()
            return redirect('signin')
            
            
        else:
             messages.info(request,'password is not matching')
             return redirect('signup')
             
    
    
    else:
         return render(request,'signup.html')


def signin(request):

    if request.method=="post":
        username=request.post['username']
        password=request.post['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            authenticate.login(request,user)
            return redirect('home')


        else:
            messages.info(request,'user and pasword not exists')  
            return redirect('signup')  


    else:
        return render(request,'signin.html')


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect('signin')
   

def user_bio(request):
    if request.method=='post':
        if request.FILES.get('image')==None:
            image=request.FILES.get('image')
            bio=request.POST['bio']
            location=request.POST['location']

            account_profile.bio=bio
            account_profile.profile_image=image
            account_profile.location=location
            account_profile.save()

    return render(request,'user_bio')



    if request.method =="POST":
        user=request.user.username
        image=request.Files.get('image')
        caption=request.Post(caption)

        post=Post.objects.create(user=user,image=image,caption=caption)

        post.save()

        return redirect('home')

    else:
        return redirect('home')    
