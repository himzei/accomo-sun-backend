from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField(blank=True, null=True,)
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey(
        "categories.Category", on_delete=models.SET_NULL, blank=True, null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "놀거리"


class Perk(CommonModel):

    """ What is included in Experience """

    name = models.CharField(max_length=100, )
    details = models.CharField(max_length=250, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "특전"
