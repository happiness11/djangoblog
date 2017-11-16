from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from.forms import UserLoginForm
from.forms import UserRegistrationForm
from blog.views import blogposts

# Create your views here.
def get_index(request):
    return render(request, 'index.html')
    
# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(blogposts)
    
    
def login(request):
    if request.method=="POST":
       form=UserLoginForm(request.POST) 
       if form.is_valid():
          user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])

          if user is not None:
                auth.login(request, user)
                messages.error(request,"You have successfully logged in")
                
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(profile)
          else:
              form.add_error (None, "You username or password was not recognised")
                
          return redirect(get_index)
        
    else:
        form = UserLoginForm()
    
    return render(request, "login.html", {'form': form})
    
    
def register(request):
    if request.method=="POST":
         form = UserRegistrationForm(request.POST)
         
         if form.is_valid():
             user = form.save()
             user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'])
             if user is not None:
                auth.login(request, user)
                return redirect(get_index)
    else:
        form = UserRegistrationForm()
    
    
    return render(request,"register.html", {'form': form})
    
@login_required()  
def profile(request):
    return render(request, 'profile.html')
    