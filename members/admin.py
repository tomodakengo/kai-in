from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Member

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('membership_number', 'full_name', 'full_name_kana', 'status', 'phone_number')
    list_filter = ('status', 'created_at')
    search_fields = ('membership_number', 'first_name', 'last_name', 
                    'first_name_kana', 'last_name_kana', 'phone_number')
    ordering = ('last_name_kana', 'first_name_kana')
    
    fieldsets = (
        (_('基本情報'), {
            'fields': (
                'user', 'membership_number', 'status',
                ('last_name', 'first_name'),
                ('last_name_kana', 'first_name_kana'),
                'birth_date',
            )
        }),
        (_('連絡先'), {
            'fields': (
                'phone_number',
                'address',
            )
        }),
        (_('緊急連絡先'), {
            'fields': (
                'emergency_contact_name',
                'emergency_contact_phone',
            )
        }),
    )
    
    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = _('氏名')
    
    def full_name_kana(self, obj):
        return obj.full_name_kana
    full_name_kana.short_description = _('氏名（カナ）')
