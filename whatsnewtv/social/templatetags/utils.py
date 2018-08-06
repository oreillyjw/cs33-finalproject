import datetime

from django.template import Library
from django.template.defaultfilters import stringfilter
from django.contrib.humanize.templatetags.humanize import intcomma

register = Library()

@register.filter(name='parse_date')
def parse_date(value):
    try:
        return datetime.datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return None
@register.filter(name='currency')
def currency(dollars):
    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])
