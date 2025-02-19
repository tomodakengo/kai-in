from django.urls import path
from . import views

app_name = 'associations'

urlpatterns = [
    path('', views.association_list, name='list'),
    path('create/', views.association_create, name='create'),
    path('<int:pk>/', views.association_detail, name='detail'),
    path('<int:pk>/update/', views.association_update, name='update'),
    path('<int:pk>/members/', views.association_members, name='members'),
    path('<int:pk>/members/add/', views.association_member_add, name='member_add'),
    path('<int:pk>/members/<int:member_pk>/remove/', views.association_member_remove, name='member_remove'),
]
