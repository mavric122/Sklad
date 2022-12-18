from django.apps import AppConfig


class TovarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tovar'
    verbose_name = 'Товары'


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category'
    verbose_name = 'Категории'
