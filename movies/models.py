from django.db import models


class CategoryRating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20, choices=CategoryRating.choices, default=CategoryRating.G
    )
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="movies"
    )
