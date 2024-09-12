from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls'), name='api'),
    path('admin/', admin.site.urls),
    path('', include('goods.urls'), name='goods'),
    path('users/', include('users.urls'), name='users'),
    path('api-auth/', include('rest_framework.urls')),
]
