from django.shortcuts import render
from django.views.generic import TemplateView
from playlist.models import Artist, Album, Track
from playlist.forms import ArtistForm


class StorefrontView(TemplateView):
    template_name = 'storefront.html'

    def get_context_data(self):
        return {
            'albums': Album.objects.all()
        }


def artist_view(request):
    form = ArtistForm()
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArtistForm()
    return render(request, 'artist_view.html', {
        'artists': Artist.objects.all(),
        'form': form
    })

def artist_detail_view(request, pk):
    return render(request, 'artist_detail_view.html', {
        'artist': Artist.objects.get(pk=pk)
    })