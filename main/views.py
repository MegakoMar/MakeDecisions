from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views.generic import UpdateView

def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def profile(request):
    return render(request, 'main/profile.html')

def profileEdit(request):
    form = UserForm()
    data = {
        'form': form
    }
    return render(request, 'main/profile_edit.html', data)
    
class ProfileUpdate(UpdateView):
    model = User
    template_name = 'main/profile_edit.html'
    
    form_class = UserForm