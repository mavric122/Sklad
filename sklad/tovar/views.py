from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import F
from .forms import TovarForm, CategoryForm

from .models import Tovar, Category


def title_site(request):
    return render(request, 'tovar/title.html')


def sklad(request):
    tovar = Tovar.objects.all()
    context = {
        'tovar': tovar
    }
    return render(request, 'tovar/sklad.html', context)


def tovar_list_category(request):
    all_category = Category.objects.all()
    context = {
        'all_category': all_category,
    }
    return render(request, 'tovar/tovar_category.html', context)


# Получение ссылки на категорию
def tovar_get_category(request, category_id):
    tovar = Tovar.objects.filter(category_id=category_id)
    all_tovar = Tovar.objects.all()
    all_category = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'all_category': all_category,
        'tovar': tovar,
        'category': category,
        'all_tovar': all_tovar
    }
    return render(request, 'tovar/list_tovar.html', context)


def all_tovars(request):
    tovar = Tovar.objects.all()
    all_category = Category.objects.all()

    context = {
        'all_category': all_category,
        'tovar': tovar
    }
    return render(request, 'tovar/list_tovar.html', context)


# Просмотр конкретного товара по его id
def view_tovar(request, tovar_id):
    tovar_items = Tovar.objects.get(pk=tovar_id)
    history = Tovar.history.filter(id=tovar_id)
    context = {
        'tovar': tovar_items,
        'history': history,

    }
    return render(request, 'tovar/tovar_id.html', context)

# Кнопка работает, но в историю не записывает.
# def increasecounter(request):
#     _reponse = Tovar.objects.update(amount=F('amount') - 1)
#     return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


def edit_tovar(request, tovar_id):
    tovar_items = Tovar.objects.get(pk=tovar_id)
    tovar_edit = get_object_or_404(Tovar, pk=tovar_id)
    if request.method == 'GET':  # Выводим заполненую форму для последующей её изменении.
        sample_form = Tovar.objects.get(pk=tovar_id)
        form = TovarForm(instance=sample_form)  # форма с нужными данными из шаблона.
    else:  # Сохраняем в базе новые значения
        new_form = Tovar.objects.get(id=tovar_id)
        form = TovarForm(request.POST, instance=new_form)
        if form.is_valid():
            form.save()
        return redirect(tovar_edit)

    content = {
        'tovar': tovar_items,
        'form': form,
        'tovar_id': tovar_id
    }

    return render(request, 'tovar/edit_tovar.html', content)


def add_category(request):
    if request.method == 'POST':  # Добавление позиции в базу
        form = CategoryForm(request.POST)
        if form.is_valid():  # Валидация формы
            category = Category.objects.create(**form.cleaned_data)
            return redirect(category)
    else:
        form = CategoryForm()

    return render(request, 'tovar/add_category.html', {'form': form})


def add_tovar(request):
    if request.method == 'POST':  # Добавление позиции в базу
        form = TovarForm(request.POST)
        if form.is_valid():  # Валидация формы
            tovar = Tovar.objects.create(**form.cleaned_data)
            return redirect(tovar)
    else:
        form = TovarForm()

    return render(request, 'tovar/add_tovar.html', {'form': form})
