from django import template
from django.db.models import Prefetch

from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('template_tags/menu.html', takes_context=True)
def draw_menu(context, slug):
    try:
        menu = Menu.objects.prefetch_related('items__items__items__items').get(slug=slug)
        return {'menu': menu, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}

