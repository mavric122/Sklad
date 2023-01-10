import requests
from django import template

from tovar.models import Category, Tovar
from tovar.views import ViewTovar

register = template.Library()  # Регистрация templatetag


@register.simple_tag()
def get_category():
    return Category.objects.all()


@register.simple_tag()
def raznica():
    histor = Tovar.history.filter(id=1)
    my_list = []
    for item in histor:
        s = item.amount
        my_list.append(s)

    print(my_list)

    list_of_unique_numbers = []
    unique_numbers = set(my_list)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    print(list_of_unique_numbers)

    return list_of_unique_numbers






