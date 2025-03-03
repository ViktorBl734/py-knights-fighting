KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {"name": "Berserk", "effect":
                                      {"power": 15, "hp": -5,
                                       "protection": 10}}, },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}},
    },
}


def apply_bonuses(knight: dict) -> None:
    knight["protection"] = sum(a["protection"]
                               for a in knight.get("armour", []))
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"]:
        effect = knight["potion"]["effect"]
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)


def battle(knightsconfig: dict) -> None:
    knights = {name: data.copy() for name, data in knightsconfig.items()}

    for knight in knights.values():
        apply_bonuses(knight)

    def fight(knight1: dict, knight2: dict) -> None:
        knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])
        knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])
        knight1["hp"] = max(0, knight1["hp"])
        knight2["hp"] = max(0, knight2["hp"])

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight["name"]: knight["hp"] for knight in knights.values()}


print(battle(KNIGHTS))
