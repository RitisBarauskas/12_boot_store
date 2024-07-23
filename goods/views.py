from random import choices

from django.http import Http404, HttpResponse
from django.shortcuts import render

from goods.constants import DATABASE, MAX_GOODS_PER_PAGE


def index(request):
    goods = choices(DATABASE.get('goods'), k=MAX_GOODS_PER_PAGE)
    return render(request, 'goods/index.html', {'goods': goods})


def category_list(request):
    return HttpResponse('Category list')


def category_detail(request, category_slug):
    return HttpResponse(f'Category detail: {category_slug}')


def good_detail(request, good_id):
    goods = DATABASE.get('goods')
    good = next((good for good in goods if good.get('id') == good_id), None)
    if not good:
        raise Http404()

    return render(request, 'goods/good_detail.html', {'good': good})