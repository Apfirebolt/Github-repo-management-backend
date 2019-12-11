from django import template

register = template.Library()


def cut(value, arg):

    """This would return favourite / unfavourite depending on value"""
    if value:
        return 'Remove From Favourites'
    else:
        return 'Add to Favourites'
