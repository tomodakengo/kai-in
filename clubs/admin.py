from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Club, ClubMember

# Register your models here.

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'association', 'status', 'is_certified', 'representative')
    list_filter = ('status', 'is_certified', 'association', 'created_at')
    search_fields = ('name', 'representative__first_name', 'representative__last_name')
    ordering = ('name',)
    
    fieldsets = (
        (_('基本情報'), {
            'fields': (
                'name',
                'association',
                'status',
                'is_certified',
                'description',
            )
        }),
        (_('代表者・設立'), {
            'fields': (
                'representative',
                'establishment_date',
            )
        }),
        (_('連絡先'), {
            'fields': (
                'address',
                'phone',
                'email',
                'website',
            )
        }),
    )

@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'club', 'role', 'joined_date', 'is_active')
    list_filter = ('role', 'is_active', 'joined_date', 'club')
    search_fields = ('member__first_name', 'member__last_name', 
                    'member__membership_number', 'club__name')
    ordering = ('-joined_date',)
    
    fieldsets = (
        (_('所属情報'), {
            'fields': (
                'club',
                'member',
                'role',
                'joined_date',
                'is_active',
            )
        }),
    )
