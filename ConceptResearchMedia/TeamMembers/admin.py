from django.contrib import admin
from .models import TeamMembers
# Register your models here.


class TeamMembersAdmin(admin.ModelAdmin):
    class Media:
        js = ('JS/tinyMce.js',)

admin.site.register(TeamMembers, TeamMembersAdmin)