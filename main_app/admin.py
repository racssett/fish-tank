from django.contrib import admin

from .models import Fish, Feeding, Enrichment

admin.site.register(Fish)
admin.site.register(Feeding)
admin.site.register(Enrichment)