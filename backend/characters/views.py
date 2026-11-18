
from bson import ObjectId
from django.http import JsonResponse
from django.shortcuts import render

from .models import Character
from .ai_summary import generate_summary
from .ai_recommendations import recommend
from .ai_questions import answer_question, MAX_QUESTION_LENGTH


# Character List, Search, and Filtering
def character_list(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    characters = Character.objects.all()
    name_query = request.GET.get("q", "").strip()
    powers_query = request.GET.get("powers", "").strip()
    category_query = request.GET.get("category", "").strip()

    if name_query:
        characters = characters.filter(name__icontains=name_query)

    if powers_query:
        characters = characters.filter(powers__icontains=powers_query)

    if category_query:
        characters = characters.filter(category__iexact=category_query)

    characters = characters.order_by("name")

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


# Individual Character Profile
def character_detail(request, character_id):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    character = (
        Character.objects.filter(id=ObjectId(character_id)).first()
        if ObjectId.is_valid(character_id)
        else None
    )

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


# Marvel Clash Website
def roster_page(request):
    return render(request, "characters/index.html")


# US-10: AI Character Summary
def character_summary(request, character_id):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    character = (
        Character.objects.filter(id=ObjectId(character_id)).first()
        if ObjectId.is_valid(character_id)
        else None
    )

    if character is None:
        return JsonResponse({
            "error": {
                "code": "character_not_found",
                "message": "Character not found."
            }
        }, status=404)

    character_data = {
        "name": character.name,
        "description": character.description,
        "powers": character.powers,
        "category": character.category,
    }

    result = generate_summary(character_data)

    return JsonResponse({
        "character_id": str(character.id),
        "character_name": character.name,
        "summary": result["summary"],
        "source": result["source"],
        "prompt_version": result["prompt_version"],
    })


# US-11: grounded character recommendations
def character_recommendations(request, character_id):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    if not ObjectId.is_valid(character_id):
        return JsonResponse({"error": "Character not found"}, status=404)
    character = Character.objects.filter(id=ObjectId(character_id)).first()
    if character is None:
        return JsonResponse({"error": "Character not found"}, status=404)
    selected = {"id": str(character.id), "name": character.name,
                "description": character.description, "powers": character.powers,
                "category": character.category}
    roster = [
        {"id": str(c.id), "name": c.name, "description": c.description,
         "powers": c.powers, "category": c.category}
        for c in Character.objects.all()
    ]
    result = recommend(selected, roster)
    return JsonResponse({"character_id": selected["id"], **result})


# US-12: ask a question about one stored character (POST only).
def character_question(request, character_id):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    if not ObjectId.is_valid(character_id):
        return JsonResponse({"error": "Character not found"}, status=404)
    character = Character.objects.filter(id=ObjectId(character_id)).first()
    if character is None:
        return JsonResponse({"error": "Character not found"}, status=404)
    import json
    if len(request.body) > 4096:
        return JsonResponse({"error": "Question payload too large"}, status=413)
    try:
        payload = json.loads(request.body)
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    if not isinstance(payload, dict):
        return JsonResponse({"error": "Invalid question"}, status=400)
    question = payload.get("question")
    if not isinstance(question, str) or not 1 <= len(question.strip()) <= MAX_QUESTION_LENGTH:
        return JsonResponse({"error": "Question must be 1 to 300 characters"}, status=400)
    record = {"name": character.name, "description": character.description,
              "powers": character.powers, "category": character.category}
    result = answer_question(record, question.strip())
    return JsonResponse({"character_id": str(character.id),
                         "character_name": character.name, **result})
