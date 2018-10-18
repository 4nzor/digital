from django import template

from first.models import Account, Org

register = template.Library()


@register.simple_tag(takes_context=True)
def jquery_set_1_1(context):
    if context.request.path != '/stipot/profile/lectures/':
        jq_path = 'libs/jquery/jquery-1.11.1.min.js'
        return jq_path
    else:
        pass
