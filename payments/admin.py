from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import PaymentPlan, Subscription, Payment

# Register your models here.

@admin.register(PaymentPlan)
class PaymentPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'currency', 'interval', 'is_active')
    list_filter = ('interval', 'is_active', 'currency')
    search_fields = ('name', 'description')
    ordering = ('name',)
    
    fieldsets = (
        (_('基本情報'), {
            'fields': (
                'name',
                'description',
                'is_active',
            )
        }),
        (_('料金'), {
            'fields': (
                'amount',
                'currency',
                'interval',
            )
        }),
        (_('Stripe情報'), {
            'fields': (
                'stripe_price_id',
            )
        }),
    )

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('member', 'plan', 'status', 'current_period_start', 'current_period_end')
    list_filter = ('status', 'plan', 'current_period_start')
    search_fields = ('member__first_name', 'member__last_name', 
                    'member__membership_number', 'stripe_subscription_id')
    ordering = ('-current_period_start',)
    
    fieldsets = (
        (_('サブスクリプション情報'), {
            'fields': (
                'member',
                'plan',
                'status',
                'stripe_subscription_id',
            )
        }),
        (_('期間'), {
            'fields': (
                'current_period_start',
                'current_period_end',
            )
        }),
    )

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'amount', 'currency', 'status', 'paid_at')
    list_filter = ('status', 'currency', 'paid_at')
    search_fields = ('stripe_payment_intent_id', 'subscription__member__membership_number')
    ordering = ('-created_at',)
    
    fieldsets = (
        (_('支払い情報'), {
            'fields': (
                'subscription',
                'amount',
                'currency',
                'status',
            )
        }),
        (_('Stripe情報'), {
            'fields': (
                'stripe_payment_intent_id',
                'paid_at',
            )
        }),
    )
