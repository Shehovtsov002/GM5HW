from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)

    def movies_count(self):
        return self.movies.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def rating(self):
        total_stars = sum(review.stars for review in self.reviews.all())
        if total_stars == 0:
            return 0
        average_rating = total_stars / len(self.reviews.all())
        return average_rating

    def __str__(self):
        return self.title


STARS = ((star, '* ' * star) for star in range(1, 6))


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(null=True, default=1, choices=STARS)

    def __str__(self):
        return self.text
