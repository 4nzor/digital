from django import template

from first.models import Account, Org

register = template.Library()


@register.simple_tag(takes_context=True)
def profile(context):
    user = context.request.user
    try:
        Account.objects.get(username=user)
        return '/profile/lecturer/'
    except Account.DoesNotExist:
        return '/profile/organizer/'


@register.simple_tag(takes_context=True)
def url_reg(context, url):
    if context.request.path == url:
        return 'active_reg'


@register.simple_tag(takes_context=True)
def url_menu(context, url):
    if context.request.path == url:
        return 'active-button'


@register.simple_tag(takes_context=True)
def get_full_name(context):
    try:
        acc = Account.objects.get(username=context.request.user)
        return acc.full_name
    except Account.DoesNotExist:
        org = Org.objects.get(username=context.request.user)
        return org.full_name
