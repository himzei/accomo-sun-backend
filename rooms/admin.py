from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "kind", "owner",)
    list_filter = ("country", "city", "pet_friendly",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)
    list_fileter = ("name", "description", "created_at")
    readonly_fields = ("created_at", "updated_at",)
