from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
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

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Artist


class ArtistApiView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        arist_serializer = ArtistSerializer(instance=artists, many=True)
        return Response(data=arist_serializer.data)
    
    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data=serializer.errors, status=400)