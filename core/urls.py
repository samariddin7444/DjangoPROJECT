from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('google/', include('app_main.urls')),
    path('users/', include('app_users.urls')),

]
