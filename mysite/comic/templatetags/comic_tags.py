from django.shortcuts import get_object_or_404, render
from django import template
from ..models import Post
register = template.Library()
@register.inclusion_tag('comic/post/daily_feature.html')

def daily_feature():
    latest_comic = Post.published.first()
    return {'latest_comic' : latest_comic}
