from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class GameUserManager(BaseUserManager):
    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError("Users must have a name")

        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(name, password, **extra_fields)


class GameUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150, unique=True)

    hours_played = models.IntegerField(default=0)
    
    achievements = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = GameUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Hero(models.Model):
    hero_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.hero_name



class Ability(models.Model):
    hero = models.ForeignKey(Hero, related_name='abilities', on_delete=models.CASCADE)
    ability_name = models.CharField(max_length=255)
    ability_description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.ability_name} ({self.hero.hero_name})"
