from django import forms
from .models import Association, AssociationMember

class AssociationForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = [
            'name',
            'code',
            'type',
            'parent',
            'description',
            'address',
            'phone',
            'email',
            'website',
            'is_active',
        ]

class AssociationMemberForm(forms.ModelForm):
    class Meta:
        model = AssociationMember
        fields = [
            'member',
            'is_staff',
            'role',
            'joined_at',
        ]
        widgets = {
            'joined_at': forms.DateInput(attrs={'type': 'date'}),
        }
