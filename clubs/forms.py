from django import forms
from .models import Club, ClubMember

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'name',
            'association',
            'representative',
            'establishment_date',
            'description',
            'address',
            'phone',
            'email',
            'website',
            'status',
            'is_certified',
        ]
        widgets = {
            'establishment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ClubMemberForm(forms.ModelForm):
    class Meta:
        model = ClubMember
        fields = [
            'member',
            'role',
            'is_active',
            'joined_at',
        ]
        widgets = {
            'joined_at': forms.DateInput(attrs={'type': 'date'}),
        }
