from django.contrib import admin
from django.urls import path
from playlist.views import StorefrontView, artist_view, artist_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('storefront', StorefrontView.as_view()),
    path('artists', artist_view),
    path('artist/<int:pk>', artist_detail_view)
]
