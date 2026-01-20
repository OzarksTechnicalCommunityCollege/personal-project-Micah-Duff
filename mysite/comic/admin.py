from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','comic_img','author','publish','status']
    list_filter = ['status', 'created','publish','author']
    search_fields = ['title','body']
    prepopulated_fields = {'comic_img': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    show_facets = admin.ShowFacets.ALWAYS