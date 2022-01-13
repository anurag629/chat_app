from django.contrib import admin
from django.urls import path
from personal.views import (
    home_screen_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
]
