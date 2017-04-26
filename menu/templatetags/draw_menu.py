from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('template_tags/menu.html', takes_context=True)
def draw_menu(context, slug):
    menu = Menu.objects.prefetch_related('items__items__items__items').get(slug=slug)
    return {'menu': menu, 'context': context}

