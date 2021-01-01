from django import forms
from playlist.models import Artist


class ArtistForm(forms.ModelForm):
    year_founded = forms.CharField(required=True)
    class Meta:
        model = Artist
        exclude = []