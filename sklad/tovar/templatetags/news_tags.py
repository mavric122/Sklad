from django import template

from tovar.models import Category

register = template.Library()  # Регистрация templatetag


@register.simple_tag()
def get_category():
    return Category.objects.all()
