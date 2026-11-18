"""Epic 5 server endpoints; intentionally separate from Epic 3 auth code."""
import json

from bson import ObjectId
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .brawl import InvalidMatchup, simulate
from .models import Character


@login_required
def brawl_page(request):
    return render(request, "characters/brawl.html")


@login_required
@require_POST
def start_brawl(request):
    if len(request.body) > 2048:
        return JsonResponse({"error": "Request too large."}, status=413)
    try:
        payload = json.loads(request.body)
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON."}, status=400)
    if not isinstance(payload, dict):
        return JsonResponse({"error": "Expected a JSON object."}, status=400)
    first_id, second_id = payload.get("fighter1"), payload.get("fighter2")
    if not all(isinstance(v, str) and ObjectId.is_valid(v) for v in (first_id, second_id)):
        return JsonResponse({"error": "Select two valid fighters."}, status=400)
    if first_id == second_id:
        return JsonResponse({"error": "Choose two different fighters."}, status=400)
    selected = list(Character.objects.filter(id__in=[ObjectId(first_id), ObjectId(second_id)]))
    by_id = {str(character.id): character for character in selected}
    if len(by_id) != 2 or first_id not in by_id or second_id not in by_id:
        return JsonResponse({"error": "One or both fighters were not found."}, status=404)
    try:
        result = simulate(
            {"id": first_id, "name": by_id[first_id].name},
            {"id": second_id, "name": by_id[second_id].name},
        )
    except InvalidMatchup as exc:
        return JsonResponse({"error": str(exc)}, status=400)
    return JsonResponse(result)
