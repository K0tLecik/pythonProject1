from django.contrib import admin

# Register your models here.
from .models import Person, Team, Position

admin.site.register(Team)


class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ["date_added"]
    ordering = ['second_name']
    list_display = ['first_name', 'second_name', 'gender', 'position_with_id']
    list_filter = ['date_added', 'position']

    @admin.display(description='Position (id)')
    def position_with_id(self, obj):
        return f"{obj.position} ({obj.position.id})"


admin.site.register(Person, PersonAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_filter = ['name']


admin.site.register(Position, PositionAdmin)
