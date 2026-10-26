from django.contrib import admin
from .models import *

# Register your models here.

admin.register(Agentname)
admin.register(AnnouncedLgaResults)
admin.register(AnnouncedPuResults)
admin.register(AnnouncedStateResults)
admin.register(AnnouncedWardResults)
admin.register(Lga)
admin.register(Party)
admin.register(PollingUnit)
admin.register(States)
admin.register(Ward)