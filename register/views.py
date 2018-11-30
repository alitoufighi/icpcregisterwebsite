from django.shortcuts import render
from register.forms import RegistrationForm


def accept(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # print("VALID FORM")
            return render(request, 'done.html')
        else:
            return render(request, 'signup.html', {'errors': form.errors})

    # print("INVALID FORM")
    return render(request, 'signup.html')
