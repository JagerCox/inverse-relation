from django import template

register = template.Library()

@register.filter(name='class_css')
def class_css(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='label_css')
def label_css(value, arg):
    return value.as_widget(label=arg)