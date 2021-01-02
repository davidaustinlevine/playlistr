from django.contrib import admin
from django.urls import path, include
from playlist.views import StorefrontView, artist_view, artist_detail_view, ArtistApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('storefront', StorefrontView.as_view()),
    path('artists', artist_view, name='artist_view'),
    path('artist/<int:pk>', artist_detail_view),
    path('api-auth/', include('rest_framework.urls')),
    path('artist-api', ArtistApiView.as_view())

]
