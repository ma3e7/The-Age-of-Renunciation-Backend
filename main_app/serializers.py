from rest_framework import serializers
from .models import Hero, Ability, GameUser

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        # Uklonjeno 'ability_image_url'
        fields = ['id', 'hero', 'ability_name', 'ability_description']

class HeroSerializer(serializers.ModelSerializer):
    abilities = AbilitySerializer(many=True, read_only=True)
    class Meta:
        model = Hero
        # Uklonjeno 'hero_image_url'
        fields = ['id', 'hero_name', 'description', 'abilities']

class GameUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameUser
        fields = ['id', 'name', 'hours_played', 'achievements', 'created_at']
        read_only_fields = ['id', 'created_at']
