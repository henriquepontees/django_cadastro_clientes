
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'base'

urlpatterns = [
    path('', ViagensView.as_view(), name='index'),
    path('health_check/', health_check, name='health_check'),
]
