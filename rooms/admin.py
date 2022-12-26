from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
    list_display = ("name", "price", "kind", "owner",
                    "total_amenities", "rating",)
    list_filter = ("country", "city", "pet_friendly",)
    search_fields = ("owner__username",)

    # def total_amenities(self, room):
    #     count = room.amenities.count()
    #     if count == 0:
    #         return "No Reviews"
    #     else:
    #         total_rating = 0
    #         for review in room.reviews.all().values("rating"):
    #             total_rating += review("rating")
    #         return round(total_rating / count, 2)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)
    list_fileter = ("name", "description", "created_at")
    readonly_fields = ("created_at", "updated_at",)
