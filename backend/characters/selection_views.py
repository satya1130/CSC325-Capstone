"""US-09: a session-scoped character selection.

The selected character id is kept in the Django session, so it works for guests
and members and survives navigation between pages until it is changed, removed,
or the session ends. Brawl fighter selection (US-13) is separate and untouched.
"""
import json

from bson import ObjectId
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Character

SESSION_KEY = "selected_character_id"


def _serialize(character):
    return {
        "id": str(character.id),
        "name": character.name,
        "description": character.description,
        "powers": character.powers,
        "image_ref": character.image_ref,
        "category": character.category,
    }


def _current(request):
    selected_id = request.session.get(SESSION_KEY)
    if not selected_id or not ObjectId.is_valid(selected_id):
        return None
    return Character.objects.filter(id=ObjectId(selected_id)).first()


@require_http_methods(["GET", "POST", "DELETE"])
def character_selection(request):
    if request.method == "GET":
        character = _current(request)
        return JsonResponse({"selected": _serialize(character) if character else None})

    if request.method == "DELETE":
        request.session.pop(SESSION_KEY, None)
        return JsonResponse({"selected": None})

    # POST: select or change the selected character.
    if len(request.body) > 512:
        return JsonResponse({"error": "Request too large."}, status=413)
    try:
        payload = json.loads(request.body)
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON."}, status=400)
    character_id = payload.get("character_id") if isinstance(payload, dict) else None
    if not isinstance(character_id, str) or not ObjectId.is_valid(character_id):
        return JsonResponse({"error": "Choose a valid character."}, status=400)
    character = Character.objects.filter(id=ObjectId(character_id)).first()
    if character is None:
        return JsonResponse({"error": "Character not found."}, status=404)
    request.session[SESSION_KEY] = str(character.id)
    return JsonResponse({"selected": _serialize(character)})
