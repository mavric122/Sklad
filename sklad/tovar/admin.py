from django.contrib import admin
from .models import Tovar, Category
from simple_history.admin import SimpleHistoryAdmin


class TovarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'category', 'amount', 'there_is')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'color')
    list_editable = ('there_is',)
    list_filter = ('there_is', 'category', 'color')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# admin.site.register(Tovar, TovarAdmin)
# admin.site.register(Category, CategoryAdmin)

admin.site.register(Tovar, SimpleHistoryAdmin)
admin.site.register(Category, SimpleHistoryAdmin)
