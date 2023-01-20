from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class Tovar(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    color = models.ForeignKey('Color', on_delete=models.PROTECT, null=True)
    amount = models.IntegerField(default=0, verbose_name='Количество')
    number = models.IntegerField(default=False, verbose_name='Номер')
    there_is = models.BooleanField(default=False, verbose_name="В наличии?")
    data_create = models.DateTimeField(auto_now=True, verbose_name='Дата первого появления')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    history = HistoricalRecords()
    comment = models.TextField(max_length=1000, verbose_name='Комментарий', default=" ")
    raznica = models.IntegerField(default=0, verbose_name='Разница')

    def get_absolute_url(self):
        return reverse('view_tovar', kwargs={'tovar_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret


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


class Color(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('color_id', kwargs={'color_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = ['title']
