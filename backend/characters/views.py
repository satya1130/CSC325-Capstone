
from django.http import JsonResponse
from django.shortcuts import render
from .models import Character


def character_list(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    characters = Character.objects.all().order_by("name")

    data = [
        {
            "id": str(character.id),
            "name": character.name,
            "description": character.description,
            "powers": character.powers,
            "image_ref": character.image_ref,
            "category": character.category,
        }
        for character in characters
    ]

    return JsonResponse({"characters": data})


def character_detail(request, character_id):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    character = Character.objects.filter(
        id=character_id
    ).first()

    if character is None:
        return JsonResponse({
            "error": {
                "code": "character_not_found",
                "message": "Character not found."
            }
        }, status=404)

    return JsonResponse({
        "id": str(character.id),
        "name": character.name,
        "description": character.description,
        "powers": character.powers,
        "image_ref": character.image_ref,
        "category": character.category,
    })


def roster_page(request):
    return render(request, "characters/index.html")
