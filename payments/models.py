from django.db import models
from django.utils.translation import gettext_lazy as _

class PaymentPlan(models.Model):
    name = models.CharField(_('プラン名'), max_length=100)
    description = models.TextField(_('説明'))
    amount = models.DecimalField(_('金額'), max_digits=10, decimal_places=0)
    currency = models.CharField(_('通貨'), max_length=3, default='JPY')
    interval = models.CharField(
        _('支払い間隔'),
        max_length=20,
        choices=[
            ('monthly', _('月次')),
            ('yearly', _('年次')),
        ],
        default='yearly'
    )
    stripe_price_id = models.CharField(_('Stripe価格ID'), max_length=100)
    is_active = models.BooleanField(_('有効'), default=True)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        verbose_name = _('支払いプラン')
        verbose_name_plural = _('支払いプラン')

    def __str__(self):
        return f"{self.name} ({self.get_interval_display()})"

class Subscription(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('有効')
        PAST_DUE = 'past_due', _('支払い遅延')
        CANCELED = 'canceled', _('キャンセル')
        UNPAID = 'unpaid', _('未払い')

    member = models.ForeignKey(
        'members.Member',
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name=_('会員')
    )
    plan = models.ForeignKey(
        PaymentPlan,
        on_delete=models.PROTECT,
        related_name='subscriptions',
        verbose_name=_('プラン')
    )
    status = models.CharField(
        _('ステータス'),
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    stripe_subscription_id = models.CharField(
        _('Stripeサブスクリプションid'),
        max_length=100,
        unique=True
    )
    current_period_start = models.DateTimeField(_('現在の期間開始日'))
    current_period_end = models.DateTimeField(_('現在の期間終了日'))
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        verbose_name = _('サブスクリプション')
        verbose_name_plural = _('サブスクリプション')

    def __str__(self):
        return f"{self.member} - {self.plan}"

class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', _('処理中')
        SUCCEEDED = 'succeeded', _('成功')
        FAILED = 'failed', _('失敗')
        REFUNDED = 'refunded', _('返金済み')

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name=_('サブスクリプション')
    )
    amount = models.DecimalField(_('金額'), max_digits=10, decimal_places=0)
    currency = models.CharField(_('通貨'), max_length=3, default='JPY')
    status = models.CharField(
        _('ステータス'),
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    stripe_payment_intent_id = models.CharField(
        _('Stripe支払いインテントID'),
        max_length=100,
        unique=True
    )
    paid_at = models.DateTimeField(_('支払日時'), null=True, blank=True)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        verbose_name = _('支払い')
        verbose_name_plural = _('支払い')

    def __str__(self):
        return f"{self.subscription} - {self.amount}{self.currency}"
