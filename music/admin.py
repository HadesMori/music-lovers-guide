from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'song']

admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Comment, CommentAdmin)