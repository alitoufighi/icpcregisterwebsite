from django import forms
from .models import Team


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('c1_first_name', 'c1_last_name', 'c1_email', 'c1_college', 'c1_phone_number',
                  'c2_first_name', 'c2_last_name', 'c2_email', 'c2_college', 'c2_phone_number',
                  'c3_first_name', 'c3_last_name', 'c3_email', 'c3_college', 'c3_phone_number',
                  'name',
                  )
