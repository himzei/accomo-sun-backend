from django.db import models
from common.models import CommonModel


class WishList(CommonModel):

    name = models.CharField(max_length=150,)
    rooms = models.ManyToManyField("rooms.Room",)
    experiences = models.ManyToManyField("experiences.Experience",)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "위시리스트"
