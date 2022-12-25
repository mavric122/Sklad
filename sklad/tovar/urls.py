from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Sklad.as_view(), name='mavric'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('search/', Search.as_view(), name='search'),
    path('category/', ListCategory.as_view(), name='spisok_category'),
    path('category/<int:category_id>/', GetCategory.as_view(), name='category_id'),
    path('category/all_tovar/', AllTovars.as_view(), name='all_tovars'),
    path('tovar/id/<int:tovar_id>', ViewTovar.as_view(), name='view_tovar'),
    path('category/add_category', AddCategory.as_view(), name='add_category'),
    path('tovar/add_tovar', AddTovar.as_view(), name='add_tovar'),
    path('tovar/edit_tovar/id/<int:pk>', UpdateTovar.as_view(), name='edit_tovar'),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('increase_counter/', increasecounter, name='increase-counter')
]
# <str:search>/