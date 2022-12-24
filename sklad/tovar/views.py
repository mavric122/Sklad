from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from .forms import TovarForm, CategoryForm

from .models import Tovar, Category


class TitleSite(ListView):
    model = Tovar
    template_name = 'tovar/title.html'


class Sklad(ListView):
    model = Tovar
    template_name = 'tovar/sklad.html'


# Список категорий
class ListCategory(ListView):
    model = Category
    template_name = 'tovar/tovar_category.html'
    context_object_name = 'all_category'


# Получение ссылки на категорию
class GetCategory(ListView):
    model = Tovar
    template_name = 'tovar/list_tovar.html'
    context_object_name = 'tovar'
    extra_context = {'title': 'Категория'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Tovar.objects.filter(category_id=self.kwargs['category_id'])


class AllTovars(ListView):
    model = Tovar
    template_name = 'tovar/tovar_id.html'
    context_object_name = 'tovar'
    extra_context = {'title': 'Категория'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все товары'
        return context


# Просмотр конкретного товара по его id

class ViewTovar(DetailView):
    model = Tovar
    template_name = 'tovar/tovar_id.html'
    context_object_name = 'tovar'
    pk_url_kwarg = 'tovar_id'

    # extra_context = {'title': 'Категория'}

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context['tovar'] = Tovar.objects.get(id=self.kwargs['tovar_id'])
        context['history'] = Tovar.history.filter(id=self.kwargs['tovar_id'])
        return context


# Функциональное представление класса выше.

# def view_tovar(request, tovar_id):
#     tovar_items = Tovar.objects.get(pk=tovar_id)
#     history = Tovar.history.filter(id=tovar_id)
#     context = {
#         'tovar': tovar_items,
#         'history': history,
#
#     }
#     return render(request, 'tovar/tovar_id.html', context)


# Кнопка работает, но в историю не записывает.
# def increasecounter(request):
#     _reponse = Tovar.objects.update(amount=F('amount') - 1)
#     return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


class UpdateTovar(UpdateView):
    form_class = TovarForm
    model = Tovar
    template_name = 'tovar/edit_tovar.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("view_tovar", kwargs={"tovar_id": pk})


class AddCategory(CreateView):
    form_class = CategoryForm
    template_name = 'tovar/add_category.html'


# def add_category(request):
#     if request.method == 'POST':  # Добавление позиции в базу
#         form = CategoryForm(request.POST)
#         if form.is_valid():  # Валидация формы
#             category = Category.objects.create(**form.cleaned_data)
#             return redirect(category)
#     else:
#         form = CategoryForm()
#
#     return render(request, 'tovar/add_category.html', {'form': form})

class AddTovar(CreateView):
    form_class = TovarForm
    template_name = 'tovar/add_tovar.html'

# def add_tovar(request):
#     if request.method == 'POST':  # Добавление позиции в базу
#         form = TovarForm(request.POST)
#         if form.is_valid():  # Валидация формы
#             tovar = Tovar.objects.create(**form.cleaned_data)
#             return redirect(tovar)
#     else:
#         form = TovarForm()
#
#     return render(request, 'tovar/add_tovar.html', {'form': form})
