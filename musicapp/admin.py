from django.contrib import admin
from musicapp.models import *

class ArtisteAdmin(admin.ModelAdmin):
    list_display = ['first_name',"last_name",'age','id']

class SongAdmin(admin.ModelAdmin):
    list_display = ['title',"artiste",'date_released','likes','id']

class LyricsAdmin(admin.ModelAdmin):
    list_display = ['content',"song_id"]

admin.site.register(Artiste,ArtisteAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Lyrics, LyricsAdmin)
# Register your models here.
