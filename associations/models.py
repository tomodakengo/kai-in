from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

class Association(MPTTModel):
    class AssociationType(models.TextChoices):
        NATIONAL = 'national', _('全国協会')
        REGIONAL = 'regional', _('地方協会')
        PREFECTURAL = 'prefectural', _('都道府県協会')

    name = models.CharField(_('協会名'), max_length=100)
    type = models.CharField(
        _('協会種別'),
        max_length=20,
        choices=AssociationType.choices
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('上位協会')
    )
    code = models.CharField(_('協会コード'), max_length=20, unique=True)
    address = models.TextField(_('住所'))
    phone = models.CharField(_('電話番号'), max_length=15)
    email = models.EmailField(_('メールアドレス'))
    website = models.URLField(_('ウェブサイト'), blank=True)
    representative_name = models.CharField(_('代表者名'), max_length=100)
    established_date = models.DateField(_('設立日'))
    description = models.TextField(_('説明'), blank=True)
    is_active = models.BooleanField(_('アクティブ'), default=True)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        verbose_name = _('協会')
        verbose_name_plural = _('協会')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class AssociationMember(models.Model):
    association = models.ForeignKey(
        Association,
        on_delete=models.CASCADE,
        related_name='members',
        verbose_name=_('協会')
    )
    member = models.ForeignKey(
        'members.Member',
        on_delete=models.CASCADE,
        related_name='associations',
        verbose_name=_('会員')
    )
    joined_date = models.DateField(_('入会日'))
    is_staff = models.BooleanField(_('スタッフフラグ'), default=False)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        verbose_name = _('協会会員')
        verbose_name_plural = _('協会会員')
        unique_together = ('association', 'member')

    def __str__(self):
        return f"{self.member} - {self.association}"
