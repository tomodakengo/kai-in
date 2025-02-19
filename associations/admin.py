from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin
from .models import Association, AssociationMember

# Register your models here.

@admin.register(Association)
class AssociationAdmin(MPTTModelAdmin):
    list_display = ('name', 'type', 'code', 'parent', 'is_active')
    list_filter = ('type', 'is_active', 'created_at')
    search_fields = ('name', 'code', 'representative_name')
    ordering = ('code',)
    
    fieldsets = (
        (_('基本情報'), {
            'fields': (
                'name', 'type', 'code', 'parent', 'is_active',
                'description',
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
        (_('代表者情報'), {
            'fields': (
                'representative_name',
                'established_date',
            )
        }),
    )

@admin.register(AssociationMember)
class AssociationMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'association', 'joined_date', 'is_staff')
    list_filter = ('is_staff', 'joined_date', 'association')
    search_fields = ('member__first_name', 'member__last_name', 
                    'member__membership_number', 'association__name')
    ordering = ('-joined_date',)
    
    fieldsets = (
        (_('所属情報'), {
            'fields': (
                'association',
                'member',
                'joined_date',
                'is_staff',
            )
        }),
    )
