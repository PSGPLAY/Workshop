from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from home.forms import ProfileForm
from .models import Profile


# @login_required
def home_page(request):
    return render(request,'home/home.html')


def about(request):
    return HttpResponse("This is a simple Django app for managing students.")

# @login_required
def profile_create(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'home/profile.html', {
        'form': form,
    })