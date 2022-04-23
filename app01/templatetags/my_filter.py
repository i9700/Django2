from django import template

register = template.Library()


# 自定义过滤器
@register.filter("mobile_fmt")
def mobile_fmt(content):
    return content[:3] + "*****" + content[-3:]
