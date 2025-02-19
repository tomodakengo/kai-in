from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'membership_number',
            'status',
            'last_name',
            'first_name',
            'last_name_kana',
            'first_name_kana',
            'birth_date',
            'address',
            'phone_number',
            'emergency_contact_name',
            'emergency_contact_phone',
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
