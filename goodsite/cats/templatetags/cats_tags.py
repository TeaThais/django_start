from django import template
from cats.models import *


register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('cats/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.simple_tag()
def get_posts(filter=None):
    if not filter:
        return Cats.objects.all()
    else:
        return Cats.objects.filter(cat_id=filter)


@register.inclusion_tag('cats/posts_on_page.html')
def show_posts_on_page(filter=None, cat_selected=0):
    if not filter:
        posts = Cats.objects.all()
    else:
        posts = Cats.objects.filter(cat_id=filter)

    return {'posts': posts, 'cat_selected': cat_selected}


@register.inclusion_tag('cats/menu_items.html')
def show_menu_items():
    menu = Menu.objects.all()
    return {'menu': menu}



