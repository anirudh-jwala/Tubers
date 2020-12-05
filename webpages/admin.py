from django.contrib import admin

from .models import Slider, Team

from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    def team_member_photo(self, object):
        return format_html('<img src="{}" width="40px" />'.format(object.photo.url))

    list_display = ('id', 'team_member_photo',
                    'first_name', 'role', 'created_date')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'last_name', 'role')
    list_filter = ('role',)


admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)
