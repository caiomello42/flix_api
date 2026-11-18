from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies'
    )
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(
        Actor,
        related_name='movies'
    )
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class MovieLog(models.Model):
    ACTION_CHOICES = (
        ('create', 'Criação'),
        ('delete', 'Exclusão'),
    )

    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    movie_id = models.IntegerField()
    title = models.CharField(max_length=500)
    user = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_action_display()} de {self.title} em {self.created_at}'
