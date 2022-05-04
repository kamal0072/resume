from django import template
register=template.Library()

@register.filter(name="remove_special")
def remove_char(value,arg):
    print(value)
    print(arg)
    for char in arg:
        print(char)
        value=value.replace(char,'')
    return value