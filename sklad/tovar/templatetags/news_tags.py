import requests
from django import template

from tovar.models import Category, Tovar
from tovar.views import ViewTovar

register = template.Library()  # Регистрация templatetag


@register.simple_tag()
def get_category():
    return Category.objects.all()


@register.simple_tag()
def raznica(filter=None):
    histor = Tovar.history.filter(id=filter)
    my_list = []
    for item in histor:
        Tovar.history.raznica = item
        print(Tovar.history.raznica)
    return histor.s






