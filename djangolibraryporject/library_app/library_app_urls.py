from django.urls import path
from . import library_app_views

urlpatterns = [
    path('', library_app_views.home_view_function, name = 'home _url_nickname '),
]