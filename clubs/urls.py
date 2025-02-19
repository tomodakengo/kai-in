from django.urls import path
from . import views

app_name = 'clubs'

urlpatterns = [
    path('', views.club_list, name='list'),
    path('create/', views.club_create, name='create'),
    path('<int:pk>/', views.club_detail, name='detail'),
    path('<int:pk>/update/', views.club_update, name='update'),
    path('<int:pk>/members/', views.club_members, name='members'),
    path('<int:pk>/members/add/', views.club_member_add, name='member_add'),
    path('<int:pk>/members/<int:member_pk>/remove/', views.club_member_remove, name='member_remove'),
]
