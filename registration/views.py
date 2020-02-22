from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserAccount

# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserAccount(request.POST)
        if form.is_valid():   #check if the username is valid from the database
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for {username}!') #send a success message that account has been created for a user
            return redirect('login')
    else:
        form = UserAccount()
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')
