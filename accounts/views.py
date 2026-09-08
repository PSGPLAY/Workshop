from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from home.models import Profile


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('home_page')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {
        'form': form
    })



def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    error = None
    if request.method == 'POST':
        # Check if submitted via raw template form (username, password, confirm_password)
        if 'confirm_password' in request.POST or 'password' in request.POST:
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '')
            confirm_password = request.POST.get('confirm_password', '')

            if not username or not password:
                error = 'Please fill in all required fields.'
            elif password != confirm_password:
                error = 'Passwords do not match.'
            elif User.objects.filter(username=username).exists():
                error = 'Username already exists.'
            else:
                user = User.objects.create_user(username=username, password=password)
                Profile.objects.create(user=user)
                login(request, user)
                return redirect('home_page')
            form = RegisterForm()
        else:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                Profile.objects.create(user=user)
                login(request, user)
                return redirect('home_page')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form,
        'error': error
    })