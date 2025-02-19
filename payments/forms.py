from django import forms
from .models import PaymentPlan, Subscription

class PaymentPlanForm(forms.ModelForm):
    class Meta:
        model = PaymentPlan
        fields = [
            'name',
            'code',
            'description',
            'amount',
            'currency',
            'interval',
            'interval_count',
            'trial_period_days',
            'is_active',
        ]

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = [
            'member',
            'plan',
            'status',
            'billing_day',
            'payment_method',
            'start_date',
            'end_date',
            'cancel_at_period_end',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
