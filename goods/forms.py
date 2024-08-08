from django.forms import ModelForm

from goods.models import Good, Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'description')


class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = ('name', 'description', 'category')
