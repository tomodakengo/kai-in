from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import User

# Create your models here.

class Member(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('アクティブ')
        INACTIVE = 'inactive', _('休会中')
        WITHDRAWN = 'withdrawn', _('退会')

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='member_profile'
    )
    status = models.CharField(
        _('ステータス'),
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    membership_number = models.CharField(
        _('会員番号'),
        max_length=50,
        unique=True
    )
    first_name = models.CharField(_('名'), max_length=30)
    last_name = models.CharField(_('姓'), max_length=30)
    first_name_kana = models.CharField(_('名（カナ）'), max_length=30)
    last_name_kana = models.CharField(_('姓（カナ）'), max_length=30)
    birth_date = models.DateField(_('生年月日'))
    phone_number = models.CharField(_('電話番号'), max_length=15)
    address = models.TextField(_('住所'))
    emergency_contact_name = models.CharField(
        _('緊急連絡先名'),
        max_length=60
    )
    emergency_contact_phone = models.CharField(
        _('緊急連絡先電話番号'),
        max_length=15
    )
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        verbose_name = _('会員')
        verbose_name_plural = _('会員')

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.membership_number})"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def full_name_kana(self):
        return f"{self.last_name_kana} {self.first_name_kana}"
