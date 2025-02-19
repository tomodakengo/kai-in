from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.member_list, name='list'),
    path('create/', views.member_create, name='create'),
    path('<int:pk>/', views.member_detail, name='detail'),
    path('<int:pk>/update/', views.member_update, name='update'),
    path('profile/', views.profile, name='profile'),
]
