from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('plans/', views.payment_plan_list, name='plans'),
    path('plans/create/', views.payment_plan_create, name='plan_create'),
    path('plans/<int:pk>/', views.payment_plan_detail, name='plan_detail'),
    path('plans/<int:pk>/update/', views.payment_plan_update, name='plan_update'),
    path('subscriptions/', views.subscription_list, name='subscriptions'),
    path('subscriptions/create/', views.subscription_create, name='subscription_create'),
    path('subscriptions/<int:pk>/', views.subscription_detail, name='subscription_detail'),
    path('subscriptions/<int:pk>/cancel/', views.subscription_cancel, name='subscription_cancel'),
    path('webhook/', views.stripe_webhook, name='webhook'),
]
