from django.contrib import admin
from .models import SoccerPlayer, ExecutiveTeam, TechnicalTeam, TeamPosition, Foot


admin.site.register(SoccerPlayer)
admin.site.register(ExecutiveTeam)
admin.site.register(TeamPosition)
admin.site.register(TechnicalTeam)
admin.site.register(Foot)
