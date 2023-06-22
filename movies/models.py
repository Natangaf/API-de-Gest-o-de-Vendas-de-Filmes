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
    def __str__(self):
        return self.title

class MovieOrder(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movie_order"
    )
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_order"
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.movie} - {self.user}"