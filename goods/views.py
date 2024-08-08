from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from goods.models import Good, Category
from goods.forms import CategoryForm, GoodForm


def index(request):
    goods = Good.objects.all()
    return render(request, 'goods/index.html', {'goods': goods})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'goods/category_list.html', {'categories': categories})


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    goods = category.goods.all()
    return render(request, 'goods/category_detail.html', {'category': category, 'goods': goods})


@login_required
def goods_by_creator(request):
    goods = request.user.goods.all()
    return render(request, 'goods/goods_by_creator.html', {'goods': goods})


def good_detail(request, good_id):
    good = get_object_or_404(Good, id=good_id)
    return render(request, 'goods/good_detail.html', {'good': good})


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'goods/category_create.html'
    success_url = reverse_lazy('goods:category_list')


class GoodCreateView(LoginRequiredMixin, CreateView):
    model = Good
    form_class = GoodForm
    template_name = 'goods/good_create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
