from django.contrib import admin
from django.urls import path, include
from tovar.views import TitleSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TitleSite.as_view()),
    path('sklad/', include('tovar.urls')),
]
