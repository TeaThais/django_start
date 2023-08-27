from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import *


class CatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True    # to have 'Save' and 'Delete' buttons on top of the page as well
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    # we can add 'time_create', 'time_update', 'get_html_photo' as fields only when we added them to 'read-only'

    def get_html_photo(self, object):
        # object is a current cat in the list
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        # mark_safe serves to use tags as tags

    get_html_photo.short_description = 'Mini-photo'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Cats, CatsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Cat site'
admin.site.site_header = 'Cat site'