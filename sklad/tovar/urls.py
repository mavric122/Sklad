from django.urls import path
from .views import *

urlpatterns = [
    path('', sklad, name='mavric'),
    path('category/', tovar_list_category, name='spisok_category'),
    path('category/<int:category_id>/', tovar_get_category, name='category_id'),
    path('category/list_tovar/', all_tovars, name='all_tovars'),
    path('tovar/id/<int:tovar_id>', view_tovar, name='view_tovar'),
    path('category/add_category', add_category, name='add_category'),
    path('tovar/add_tovar', add_tovar, name='add_tovar'),
    path('tovar/edit_tovar/id/<int:tovar_id>', edit_tovar, name='edit_tovar'),
    # path('increase_counter/', increasecounter, name='increase-counter')

]
