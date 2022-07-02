from django.contrib import admin

from .models import Race, Runner, Teams

# admin.site.register(Race)
# admin.site.register(Runner)
# admin.site.register(Teams)


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    list_display = ("number", "last_name", "first_name", "start_time", "end_time", "elapsed_time")
    search_fields = ("last_name__startswith",)


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ("number", "name", "runners_A", "runners_B", "runners_C", "runners_D", "runners_E", "runners_F")


