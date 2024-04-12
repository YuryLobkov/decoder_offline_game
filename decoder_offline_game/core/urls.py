from django.urls import path
from .views import homepage_view
from . import views

urlpatterns = [
    path('', homepage_view, name='homepage'),
]