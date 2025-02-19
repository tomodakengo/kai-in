from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Notification

# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'type', 'level', 'is_read', 'created_at')
    list_filter = ('type', 'level', 'is_read', 'created_at')
    search_fields = ('title', 'message', 'user__email')
    ordering = ('-created_at',)
    
    fieldsets = (
        (_('通知内容'), {
            'fields': (
                'title',
                'message',
                'type',
                'level',
            )
        }),
        (_('送信先・状態'), {
            'fields': (
                'user',
                'is_read',
            )
        }),
    )
    
    def has_add_permission(self, request):
        # 通知は自動生成されるため、手動での追加は不可
        return False
