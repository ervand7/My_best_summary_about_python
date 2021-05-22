from datetime import datetime

from django import template


register = template.Library()


def plural_forms(n, forms: list = None):
    if not forms:
        forms = ['час', 'часа', 'часов']
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2
    return forms[p]


@register.filter
def format_date(value):
    if not type(value) in [float, int]:
        return value
    delta = datetime.now().timestamp() - value
    if delta > 86400:
        return datetime.fromtimestamp(value).strftime('%Y-%m-%d')
    elif delta > 600:
        hours = int(delta // 3600)
        return f'{hours} {plural_forms(hours)} назад'
    else:
        return 'только что'


@register.filter
def score_eval(value, text):
    if value:
        if not type(value) == int:
            return value
        if value > 5:
            return 'хорошо'
        elif value < -5:
            return 'все плохо'
        else:
            return 'нейтрально'
    else:
        return text


@register.filter
def format_num_comments(value):
    if not type(value) == int:
        return value
    if value > 50:
        return '50+'
    elif 0 < value <= 50:
        return value
    else:
        return 'Оставьте комментарий'


@register.filter
def format_selftext(value, count):
    if not type(count) == int:
        return value
    text_list = value.split()
    if len(text_list) <= count * 2 + 3:
        return value
    return f'{" ".join(text_list[:count])} ... {" ".join(text_list[-count:])}'
