from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, GoodViewSet


router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='category')
router_v1.register('goods', GoodViewSet, basename='good')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
