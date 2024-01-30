from django.contrib import admin
from django.urls import path, include
from .views import home_view
urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('banks/', include('banks.urls')),
]