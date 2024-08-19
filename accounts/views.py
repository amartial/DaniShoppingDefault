from django.contrib import messages, auth
from django.shortcuts import redirect, render

from accounts.forms import RegistrationForm
from accounts.models import Account

# Create your views here.

def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name  = form.cleaned_data['last_name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        username = email.split('@')[0]
        password = form.cleaned_data['password']

        user = Account.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )
        user.phone_number = phone_number
        user.save()
        messages.success(request, 'Registration successful.')
        return redirect('register')
    # else:
    #     # form = RegistrationForm(request.POST)
    #     print("Voici l'erreur sur le formulaire")
    #     print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')
