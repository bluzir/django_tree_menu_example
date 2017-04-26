from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_nav_active(context, path):
    if path in context.request.get_full_path():
        return 'active'
    else:
        return None


@register.inclusion_tag('template_tags/dropdown.html', takes_context=True)
def draw_dropdown(context, item):
    full_path = context.request.get_full_path()
    return {'item': item, 'full_path': full_path}

