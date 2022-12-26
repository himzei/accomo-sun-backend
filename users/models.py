from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(
        max_length=150, editable=False
    )
    last_name = models.CharField(
        max_length=150, editable=False
    )
    username = models.CharField(verbose_name="아이디", max_length=150,
                                unique=True,)

    avatar = models.URLField(blank=True, verbose_name="프로필 사진")
    name = models.CharField(max_length=150, default="", verbose_name="이름")
    email = models.EmailField(blank=True, verbose_name="이메일")
    is_host = models.BooleanField(default=False, verbose_name="호스트")
    gender = models.CharField(
        max_length=10, choices=GenderChoices.choices, verbose_name="성별")
    language = models.CharField(
        max_length=2, choices=LanguageChoices.choices, verbose_name="언어")
    currency = models.CharField(
        max_length=5, choices=CurrencyChoices.choices, verbose_name="통화단위")

    class Meta:
        verbose_name_plural = "회원"
