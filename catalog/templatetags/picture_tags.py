from django import template


register = template.Library()

@register.filter()
def media_filter(path):
    if path:
        return f"/photos/{path}"
    return "#"