from django import template

register = template.Library()

CENSOR_WORDS = [
    'scummer',
    'Еда'

]


@register.filter()
def censor(value):
    """
    text: текст к которому нужно применить фильтр
    """
    for word in CENSOR_WORDS:
        value = value.replace(word, '*' * len(word))
    return value
