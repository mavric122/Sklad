from django.contrib import admin
from django.urls import path, include
from tovar.views import title_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', title_site),
    path('sklad/', include('tovar.urls')),
]
