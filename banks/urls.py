from django.urls import path
from .views import bank_list, add_banks, bank_edit, bank_delete

urlpatterns = [
    path('', bank_list, name='bank_list'),
    path('add/', add_banks, name='add_banks'),
    path('<int:bank_id>/edit/', bank_edit, name='bank_edit'),
    path('<int:bank_id>/delete/', bank_delete, name='bank_delete'),

]
