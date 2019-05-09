from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('template_tags/menu.html', takes_context=True)
def draw_menu(context, slug):  # takes slug as argument
    try:
        # probably not best solution, but it saves us many db requests if menu is complex
        # TODO: rewrite using django.db.models.Prefetch
        menu = Menu.objects.prefetch_related('items__items__items__items').get(slug=slug)
        return {'menu': menu, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}

