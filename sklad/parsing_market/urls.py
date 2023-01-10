from django.urls import path, include
from .views import *

urlpatterns = [
    path('', title_parsing, name='parsing_market'),
    path('ozon/', ozon_title, name='ozon_title'),
    path('test/', test, name='test'),

]