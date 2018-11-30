from django.shortcuts import render
from register.forms import RegistrationForm


def accept(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'done.html')
    return render(request, 'signup.html')
