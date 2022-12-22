from django import forms
from django.forms import ModelForm
from .models import Category, Tovar


# Для примера, я сделал форму не связанную с моделью. Оставлена для примера
# Поэтому обработка формы в add_tovar in views.py имеет метод Tovar.objects.create(**form.cleaned_data)
# Это позволяет сохранить форму и связать её с моделью.

# class TovarForm(ModelForm):
# title = forms.CharField(max_length=100, label="Наименование", widget=forms.TextInput(attrs={
#     "class": "form-control"
# }))
# color = forms.CharField(max_length=50, label="Цвет", widget=forms.TextInput(attrs={
#     "class": "form-control"
# }))
# amount = forms.IntegerField(label="Количество", widget=forms.NumberInput(attrs={
#     "class": "form-control"
# }))
# number = forms.IntegerField(label="Номер", widget=forms.NumberInput(attrs={
#     "class": "form-control"
# }))
# there_is = forms.BooleanField(label="В наличии?", initial=True, widget=forms.CheckboxInput(attrs={
#     # "class": "form-check",
#     "class": "form-check-input"
# }))
# category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label=None,
#                                   widget=forms.Select(attrs={
#     "class": "form-control"
# }))

class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar  # С какой моделью будет связана форма
        fields = ['title', 'color', 'amount', 'number', 'there_is', 'category']  # Какие поля нужны из модели.
        widgets = {  # Внимание!!! В виджетах используются не аргумент для поля, а аргумент для виджета.
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'color': forms.TextInput(attrs={"class": "form-control"}),
            'amount': forms.NumberInput(attrs={"class": "form-control"}),
            'number': forms.NumberInput(attrs={"class": "form-control"}),
            'there_is': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
