from django import template

register = template.Library()


@register.filter
def get_dict_value(horizon_row_as_dict: dict, key: str) -> str:
    """Attention! In template the first parameter will go to
    function by default."""
    return horizon_row_as_dict[key]


@register.filter
def convert_str_to_float(indicator: str) -> float:
    """
    Initial type of indicators is str. We need
    float if indicator else ''
    """
    rez = float(indicator) if indicator else ...
    return rez


@register.filter
def choice_of_color(indicator: float):
    if indicator < 0:
        return "green darken-2"
    if indicator >= 5:
        return "red lighten-1"
    if indicator >= 2:
        return "red lighten-3"
    if indicator >= 1:
        return "red lighten-5"
    else:
        return "<td>"
