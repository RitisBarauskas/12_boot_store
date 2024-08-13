from django.urls import path

from goods.views import (
    CategoryCreateView,
    GoodCreateView,
    GoodListView,
    CategoryListView,
    CategoryDetailView,
    CreatorDetailView,
    GoodDetailView,
    UserProfileUpdateView,
)

app_name = 'goods'

urlpatterns = [
    path('', GoodListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<str:category_slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('good/<int:good_id>/', GoodDetailView.as_view(), name='good_detail'),
    path('good/create/', GoodCreateView.as_view(), name='good_create'),
    path('profile/', CreatorDetailView.as_view(), name='goods_by_creator'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='user_profile_update'),
]
