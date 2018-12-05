from django.shortcuts import render
from register.forms import RegistrationForm
import csv
from django.http import HttpResponse
from .models import Team


def accept(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'done.html')
        else:
            print(form.errors.items())
            if 'name' in form.errors.items():
                print("Name Error", form.errors['name'])
                error = {'name': form.errors['name']}
            else:
                print("Error!")
                error = {'error': True}
            print(error)
            return render(request, 'signup.html', error)

    return render(request, 'signup.html')


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Team Name',
        'Lead First Name', 'Lead Last name', ' Lead Email address', 'Lead Phone Number', 'Lead College',
        '2nd First Name', '2nd Last name', ' 2nd Email address', '2nd College',
        '3rd First Name', '3rd Last name', ' 3rd Email address', '3rd College',
    ])

    teams = Team.objects.all().values_list(
        'name',
        'c1_first_name', 'c1_last_name', 'c1_email', 'c1_phone_number', 'c1_college',
        'c2_first_name', 'c2_last_name', 'c2_email', 'c2_college',
        'c3_first_name', 'c3_last_name', 'c3_email', 'c3_college',
                                           )
    for team in teams:
        writer.writerow(team)

    return response
