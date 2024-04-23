from django.db import models

# Create your models here.
class EggGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    class Meta:
        app_label = 'TP_api_django'

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(null=True)
    fling_effect_id = models.IntegerField(null=True)
    class Meta:
        app_label = 'TP_api_django'

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    region_id = models.IntegerField(null=True)
    identifier = models.CharField(max_length=79)
    class Meta:
        app_label = 'TP_api_django'

class Move(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.SmallIntegerField(null=True)
    pp = models.SmallIntegerField(null=True)
    accuracy = models.SmallIntegerField(null=True)
    priority = models.SmallIntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(null=True)
    contest_type_id = models.IntegerField(null=True)
    contest_effect_id = models.IntegerField(null=True)
    super_contest_effect_id = models.IntegerField(null=True)
    class Meta:
        app_label = 'TP_api_django'

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()
    class Meta:
        app_label = 'TP_api_django'

class PokemonEggGroup(models.Model):
    species_id = models.IntegerField()
    egg_group_id = models.IntegerField()
    class Meta:
        app_label = 'TP_api_django'

class PokemonFormGeneration(models.Model):
    pokemon_form_id = models.IntegerField()
    generation_id = models.IntegerField()
    game_index = models.IntegerField()
    class Meta:
        app_label = 'TP_api_django'

class PokemonMove(models.Model):
    pokemon_id = models.IntegerField()
    version_group_id = models.IntegerField()
    move_id = models.IntegerField()
    pokemon_move_method_id = models.IntegerField()
    level = models.IntegerField()
    order = models.IntegerField(null=True)
    class Meta:
        app_label = 'TP_api_django'

class PokemonStat(models.Model):
    pokemon_id = models.IntegerField()
    stat_id = models.IntegerField()
    base_stat = models.IntegerField()
    effort = models.IntegerField()
    class Meta:
        app_label = 'TP_api_django'

class PokemonType(models.Model):
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()
    class Meta:
        app_label = 'TP_api_django'

class Stat(models.Model):
    id = models.IntegerField(primary_key=True)
    damage_class_id = models.IntegerField(null=True)
    identifier = models.CharField(max_length=79)
    is_battle_only = models.BooleanField()
    game_index = models.IntegerField(null=True)
    class Meta:
        app_label = 'TP_api_django'

class Type(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(null=True)
    class Meta:
        app_label = 'TP_api_django'
