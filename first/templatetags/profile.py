from django import template
from django.contrib.auth.models import User

from first.models import Account, Org

register = template.Library()


@register.simple_tag(takes_context=True)
def profile(context):
    user = context.request.user
    try:
        Account.objects.get(username=user)
        return '/stipot/profile/lecturer/'
    except Account.DoesNotExist:
        return '/stipot/profile/organizer/'


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
    if context.request.user.is_superuser == False:
        try:
            acc = Account.objects.get(username=context.request.user)
            return acc.full_name
        except Account.DoesNotExist:
            org = Org.objects.get(username=context.request.user)
            return org.full_name
    else:
        return User.objects.get(username=context.request.user).username
