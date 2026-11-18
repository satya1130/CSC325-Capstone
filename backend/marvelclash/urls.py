from django.contrib import admin
from django.urls import path, include
from characters.views import roster_page
from characters.brawl_views import brawl_page, start_brawl

urlpatterns = [
    path("admin/", admin.site.urls),
    path("brawl/", brawl_page, name="brawl"),
    path("api/brawl/start/", start_brawl, name="start_brawl"),
    path("", roster_page, name="roster"),
    path("api/characters/", include("characters.urls")),
]