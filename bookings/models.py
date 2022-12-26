from django.db import models
from common.models import CommonModel


class Booking(CommonModel):

    class BookingKindChoices(models.TextChoices):

        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(max_length=15, choices=BookingKindChoices.choices,)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="bookings",)
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.SET_NULL, blank=True, null=True,  related_name="bookings",)
    experience = models.ForeignKey(
        "experiences.Experience", on_delete=models.SET_NULL, blank=True, null=True,  related_name="bookings",)
    check_in = models.DateField(blank=True, null=True, )
    check_out = models.DateField(blank=True, null=True, )
    experience_time = models.DateTimeField(blank=True, null=True, )
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.kind.title()}: {self.user}"

    class Meta:
        verbose_name_plural = "예약"
