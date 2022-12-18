from django.db import models
from django.urls import reverse


class Tovar(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    number = models.IntegerField(default=False, verbose_name='Номер')
    there_is = models.BooleanField(default=False, verbose_name="В наличии?")
    data_create = models.DateTimeField(auto_now=True, verbose_name='Дата первого появления')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    # Миграция не сделана. Задел на будущее
    # comment = models.CharField(max_length=1000, verbose_name='Комментарий')
    # History ??

    def get_absolute_url(self):
        return reverse('view_tovar', kwargs={'tovar_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('category_id', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
