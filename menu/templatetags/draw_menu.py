from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('template_tags/menu.html')
def draw_menu(slug):
    menu = Menu.objects.prefetch_related('items__items').get(slug=slug)
    return {'menu': menu}

