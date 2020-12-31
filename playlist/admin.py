from django.contrib import admin
from playlist.models import Artist, Album


class ArtistAdmin(admin.ModelAdmin):
    model = Artist


class AlbumAdmin(admin.ModelAdmin):
    model = Album


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)