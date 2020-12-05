from django.contrib import admin

from .models import Youtuber

from django.utils.html import format_html


class YtAdmin(admin.ModelAdmin):

    def youtuber_photo(self, object):
        return format_html('<img src="{}" width="40px" />'.format(object.photo.url))

    list_display = ('id', 'name', 'youtuber_photo','subs_count', 'is_featured')
    search_fields = ('name', 'camera_type', 'category')
    list_filter = ('city', 'camera_type', 'category')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, YtAdmin)
