from django.urls import path

from goods.views import (
    index,
    category_list,
    category_detail,
    good_detail,
    CategoryCreateView,
    GoodCreateView,
    goods_by_creator,
)

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('category/', category_list, name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<str:category_slug>/', category_detail, name='category_detail'),
    path('good/<int:good_id>/', good_detail, name='good_detail'),
    path('good/create/', GoodCreateView.as_view(), name='good_create'),
    path('profile/', goods_by_creator, name='goods_by_creator'),
]
