from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/', include('apps.app_exemplo.urls'), name='example'),
    path('login/', include('apps.app_login.urls'), name='login'),
    path('', include('base.urls'), name='base'),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
