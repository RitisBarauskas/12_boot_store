from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from goods.models import Good, Category, User
from goods.forms import CategoryForm, GoodForm


class GoodListView(ListView):
    model = Good
    template_name = 'goods/index.html'
    context_object_name = 'goods'


class CategoryListView(ListView):
    model = Category
    template_name = 'goods/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(ListView):
    model = Good
    template_name = 'goods/category_detail.html'
    context_object_name = 'goods'
    category = None

    def load_category(self):
        if self.category is None:
            self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])

    def get_queryset(self):
        self.load_category()
        filters = Q(is_open_for_all=True)
        if self.request.user.is_authenticated:
            filters |= Q(creator=self.request.user)

        return self.category.goods.filter(filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.load_category()
        context['category'] = self.category
        return context


class CreatorDetailView(LoginRequiredMixin, ListView):
    model = Good
    template_name = 'goods/goods_by_creator.html'
    context_object_name = 'goods'

    def get_queryset(self):
        return self.request.user.goods.all()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'goods/profile_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('goods:goods_by_creator')


class GoodDetailView(DetailView):
    model = Good
    template_name = 'goods/good_detail.html'
    context_object_name = 'good'
    pk_url_kwarg = 'good_id'


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
