import os
import django
import json

# Postavljanje Django settings-a
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ageofrenunciation.settings")
django.setup()

from main_app.models import Hero, Ability

# Putanja do JSON fajla sa herojima
json_path = os.path.join(os.path.dirname(__file__), 'data', 'heroes.json')

# Učitavanje podataka iz JSON-a
with open(json_path, "r", encoding="utf-8") as f:
    heroes_data = json.load(f)

print(f"Found {len(heroes_data)} heroes in JSON")

# Brisanje postojećih heroja i njihovih ability-a
Ability.objects.all().delete()
Hero.objects.all().delete()

# Seedovanje novih heroja i ability-a
for hero_data in heroes_data:
    hero, created = Hero.objects.get_or_create(
        hero_name=hero_data["hero_name"],
        defaults={"description": hero_data.get("description", "")}
    )

    for ability_data in hero_data.get("abilities", []):
        Ability.objects.get_or_create(
            hero=hero,
            ability_name=ability_data["ability_name"],
            defaults={"ability_description": ability_data.get("ability_description", "")}
        )

print("Seeding completed!")
