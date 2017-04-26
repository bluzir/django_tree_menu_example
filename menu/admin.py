from django.contrib import admin

from menu.models import Menu, MenuParentItem, MenuChildItem

admin.site.register(Menu)
admin.site.register(MenuParentItem)
admin.site.register(MenuChildItem)

