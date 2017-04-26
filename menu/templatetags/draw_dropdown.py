from django import template

register = template.Library()


@register.inclusion_tag('template_tags/dropdown.html')
def draw_dropdown(item):
    return {'item': item}

