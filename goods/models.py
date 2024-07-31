from django.db.models import Model, CharField, SlugField, TextField, ForeignKey, SET_NULL

from goods.constants import MAX_LENGTH_CHAR_FIELD, MAX_LENGTH_SLUG_FIELD


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

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return self.name
