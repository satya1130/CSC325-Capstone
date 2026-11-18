
from django.urls import path
from . import views

urlpatterns = [
    path("", views.character_list, name="character_list"),

    path(
        "<str:character_id>/recommendations/",
        views.character_recommendations,
        name="character_recommendations"
    ),

    path(
        "<str:character_id>/ask/",
        views.character_question,
        name="character_question"
    ),

    path(
        "<str:character_id>/summary/",
        views.character_summary,
        name="character_summary"
    ),

    path(
        "<str:character_id>/",
        views.character_detail,
        name="character_detail"
    ),
]
