from django.contrib import admin

# Register your models here.
from .models.Player import Player
from .models.League import League
from .models.Tournament import Tournament
from .models.Matchup import Matchup
from .models.Game import Game

# Need to add this for each model that requires managing

admin.site.register(Player)
admin.site.register(League)
admin.site.register(Tournament)
admin.site.register(Matchup)
admin.site.register(Game)
