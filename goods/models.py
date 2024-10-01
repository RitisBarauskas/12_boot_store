from django.contrib.auth import get_user_model
from django.db.models import Model, CharField, SlugField, TextField, ForeignKey, SET_NULL, BooleanField
from django.urls import reverse

from goods.constants import MAX_LENGTH_CHAR_FIELD, MAX_LENGTH_SLUG_FIELD

User = get_user_model()


class Category(Model):
    name = CharField(max_length=MAX_LENGTH_CHAR_FIELD, verbose_name='Название')
    slug = SlugField(max_length=MAX_LENGTH_SLUG_FIELD, unique=True, verbose_name='SLUG')
    description = TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Good(Model):
    name = CharField(max_length=MAX_LENGTH_CHAR_FIELD, verbose_name='Название')
    category = ForeignKey(Category, on_delete=SET_NULL, null=True, related_name='goods', verbose_name='Категория')
    description = TextField(verbose_name='Описание')
    creator = ForeignKey(User, on_delete=SET_NULL, null=True, related_name='goods', verbose_name='Создатель')
    is_open_for_all = BooleanField(default=False, verbose_name='Открыт для всех')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods:good_detail', args=[str(self.id)])
