from django.shortcuts import render, redirect  
#Django authentication libraries           
from django.contrib.auth import authenticate, login
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth import authenticate, login, logout
#to protect function-based views
from django.contrib.auth.decorators import login_required

def login_view(request):
    error_message = None  
    form = AuthenticationForm()

    if request.method == "POST":                       
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():                                
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password') 
            user = authenticate(username = username, password = password)
            if user is not None:                    
                login(request, user)                
                return redirect('recipes:home')
        else:  
            error_message = 'ooops.. something went wrong'

    context ={                                             
        'form': form, 
        'error_message': error_message     
    }
    return render(request, 'auth/login.html', context)     
        
    
@login_required
def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html')

def welcome_view(request):
    return render(request, 'welcome/recipes_home.html')