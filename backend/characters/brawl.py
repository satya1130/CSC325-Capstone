"""Deterministic, fictional game rules. No Marvel-canon combat claims."""
from hashlib import sha256

MAX_HEALTH = 100
MAX_TURNS = 100


class InvalidMatchup(ValueError):
    pass


def simulate(first, second):
    """Two distinct dicts with id/name. Pure, reproducible and bounded."""
    if not isinstance(first, dict) or not isinstance(second, dict):
        raise InvalidMatchup("Choose two fighters.")
    if not first.get("id") or not second.get("id"):
        raise InvalidMatchup("Choose two fighters.")
    if str(first["id"]) == str(second["id"]):
        raise InvalidMatchup("Choose two different fighters.")
    for fighter in (first, second):
        if not str(fighter.get("name", "")).strip():
            raise InvalidMatchup("Both fighters must have names.")

    fighters = [
        {"id": str(f["id"]), "name": str(f["name"]), "health": MAX_HEALTH}
        for f in (first, second)
    ]
    turns = []
    for turn in range(1, MAX_TURNS + 1):
        attacker_index = (turn - 1) % 2
        defender_index = 1 - attacker_index
        attacker, defender = fighters[attacker_index], fighters[defender_index]
        # Team-designed balancing values, not sourced abilities or Marvel canon.
        token = f'{attacker["id"]}:{defender["id"]}:{turn}'.encode("utf-8")
        damage = 8 + (int.from_bytes(sha256(token).digest()[:2], "big") % 13)
        before = defender["health"]
        defender["health"] = max(0, before - damage)
        turns.append({
            "turn": turn,
            "attacker_id": attacker["id"],
            "attacker_name": attacker["name"],
            "defender_id": defender["id"],
            "defender_name": defender["name"],
            "move": "Standard attack",
            "damage": before - defender["health"],
            "health_after": defender["health"],
            "health": [fighters[0]["health"], fighters[1]["health"]],
        })
        if defender["health"] == 0:
            break
    # Every attack deals >= 8 damage; match always finishes before MAX_TURNS.
    winner = next(f for f in fighters if f["health"] > 0)
    return {
        "simulation": True,
        "disclaimer": "Unofficial fan-game simulation. Stats and attacks are game rules, not Marvel canon.",
        "rules_version": "brawl_v1",
        "fighters": fighters,
        "turns": turns,
        "winner": {"id": winner["id"], "name": winner["name"]},
    }
