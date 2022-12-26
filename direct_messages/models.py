from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):

    users = models.ManyToManyField("users.User",)

    def __str__(self):
        return "Chatting Room"

    class Meta:
        verbose_name_plural = "채팅방"


class Message(CommonModel):

    text = models.TextField()
    user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="messages",)

    room = models.ForeignKey("direct_messages.ChattingRoom",
                             on_delete=models.CASCADE, related_name="messages",)

    def __str__(self):
        return f"{self.user}: {self.text}"

    class Meta:
        verbose_name_plural = "메세지"
