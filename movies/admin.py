from django.contrib import admin
from movies.models import Movie, MovieLog


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'resume')


@admin.register(MovieLog)
class MovieLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'movie_id', 'title', 'user', 'created_at')
    list_filter = ('action',)
