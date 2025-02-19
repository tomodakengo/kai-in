from django.db import models
from django.utils.translation import gettext_lazy as _

class Club(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', _('申請中')
        APPROVED = 'approved', _('承認済み')
        REJECTED = 'rejected', _('却下')
        SUSPENDED = 'suspended', _('停止中')

    name = models.CharField(_('クラブ名'), max_length=100)
    association = models.ForeignKey(
        'associations.Association',
        on_delete=models.PROTECT,
        related_name='clubs',
        verbose_name=_('所属協会')
    )
    status = models.CharField(
        _('ステータス'),
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    is_certified = models.BooleanField(_('公認クラブ'), default=False)
    establishment_date = models.DateField(_('設立日'))
    representative = models.ForeignKey(
        'members.Member',
        on_delete=models.PROTECT,
        related_name='represented_clubs',
        verbose_name=_('代表者')
    )
    address = models.TextField(_('住所'))
    phone = models.CharField(_('電話番号'), max_length=15)
    email = models.EmailField(_('メールアドレス'))
    website = models.URLField(_('ウェブサイト'), blank=True)
    description = models.TextField(_('説明'), blank=True)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        verbose_name = _('クラブ')
        verbose_name_plural = _('クラブ')

    def __str__(self):
        return self.name

class ClubMember(models.Model):
    class Role(models.TextChoices):
        MANAGER = 'manager', _('運営者')
        INSTRUCTOR = 'instructor', _('指導者')
        MEMBER = 'member', _('メンバー')

    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name='members',
        verbose_name=_('クラブ')
    )
    member = models.ForeignKey(
        'members.Member',
        on_delete=models.CASCADE,
        related_name='clubs',
        verbose_name=_('会員')
    )
    role = models.CharField(
        _('役割'),
        max_length=20,
        choices=Role.choices,
        default=Role.MEMBER
    )
    joined_date = models.DateField(_('入会日'))
    is_active = models.BooleanField(_('アクティブ'), default=True)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        verbose_name = _('クラブ会員')
        verbose_name_plural = _('クラブ会員')
        unique_together = ('club', 'member')

    def __str__(self):
        return f"{self.member} - {self.club} ({self.get_role_display()})"
