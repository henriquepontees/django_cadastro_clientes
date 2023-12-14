from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomRedirectView

app_name = 'login'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('redirect/', CustomRedirectView.as_view(), name='redirect'),
]
