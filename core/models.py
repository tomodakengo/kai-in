from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = 'admin', _('管理者')
        STAFF = 'staff', _('協会スタッフ')
        CLUB_MANAGER = 'club_manager', _('クラブ運営者')
        INSTRUCTOR = 'instructor', _('指導者')
        COMPETITOR = 'competitor', _('競技者')
        MEMBER = 'member', _('一般会員')

    email = models.EmailField(_('メールアドレス'), unique=True)
    user_type = models.CharField(
        _('ユーザータイプ'),
        max_length=20,
        choices=UserType.choices,
        default=UserType.MEMBER
    )
    is_active = models.BooleanField(_('アクティブ'), default=True)
    date_joined = models.DateTimeField(_('登録日'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('ユーザー')
        verbose_name_plural = _('ユーザー')

    def __str__(self):
        return self.email
