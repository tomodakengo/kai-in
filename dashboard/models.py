from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Notification(models.Model):
    class Type(models.TextChoices):
        PAYMENT = 'payment', _('支払い')
        SYSTEM = 'system', _('システム')
        MEMBERSHIP = 'membership', _('会員')
        CLUB = 'club', _('クラブ')
        ASSOCIATION = 'association', _('協会')

    class Level(models.TextChoices):
        INFO = 'info', _('情報')
        WARNING = 'warning', _('警告')
        ERROR = 'error', _('エラー')

    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='notifications',
        verbose_name=_('ユーザー')
    )
    type = models.CharField(
        _('種別'),
        max_length=20,
        choices=Type.choices
    )
    level = models.CharField(
        _('レベル'),
        max_length=20,
        choices=Level.choices,
        default=Level.INFO
    )
    title = models.CharField(_('タイトル'), max_length=200)
    message = models.TextField(_('メッセージ'))
    is_read = models.BooleanField(_('既読'), default=False)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)

    class Meta:
        verbose_name = _('通知')
        verbose_name_plural = _('通知')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"
