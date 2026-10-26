from django.contrib import admin
from django.urls import path, include
from characters.views import roster_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", roster_page, name="roster"),
    path("api/characters/", include("characters.urls")),
]