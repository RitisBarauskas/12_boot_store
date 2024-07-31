from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from goods.models import Good, Category


def index(request):
    goods = Good.objects.all()
    return render(request, 'goods/index.html', {'goods': goods})


def category_list(request):
    return HttpResponse('Category list')


def category_detail(request, category_slug):
    return HttpResponse(f'Category detail: {category_slug}')


def good_detail(request, good_id):
    good = get_object_or_404(Good, id=good_id)

    return render(request, 'goods/good_detail.html', {'good': good})