from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Hero, Ability
from .serializers import HeroSerializer, AbilitySerializer, GameUserSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def all_heroes(request):
    heroes = Hero.objects.all()
    return Response(HeroSerializer(heroes, many=True).data)

@api_view(['GET'])
@permission_classes([AllowAny])
def single_hero(request, id):
    try:
        hero = Hero.objects.get(id=id)
    except Hero.DoesNotExist:
        return Response({"error": "Hero not found"}, status=404)
    return Response(HeroSerializer(hero).data)

@api_view(['GET'])
@permission_classes([AllowAny])
def hero_abilities(request, hero_id):
    abilities = Ability.objects.filter(hero_id=hero_id)
    return Response(AbilitySerializer(abilities, many=True).data)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    new_name = request.data.get("name")
    if new_name:
        user.name = new_name
    hours = request.data.get("hours_played")
    if hours is not None:
        try:
            user.hours_played = int(hours)
        except:
            pass
    achievements = request.data.get("achievements")
    if achievements is not None:
        user.achievements = achievements
    user.save()
    return Response(GameUserSerializer(user).data)
