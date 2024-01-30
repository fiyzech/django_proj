from django.urls import path
from .views import user_list, user_edit, user_delete, add_users

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<int:user_id>/edit/', user_edit, name='user_edit'),
    path('<int:user_id>/delete/', user_delete, name='user_delete'),
    path('users/', user_list, name='user_list'),
    path('users/add/', add_users, name='add_users'),
]