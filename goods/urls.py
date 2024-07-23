from django.urls import path

from goods.views import index, category_list, category_detail, good_detail

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('category/', category_list, name='category_list'),
    path('category/<str:category_slug>/', category_detail, name='category_detail'),
    path('good/<int:good_id>/', good_detail, name='good_detail'),
]