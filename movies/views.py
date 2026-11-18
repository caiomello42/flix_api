from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie, MovieLog
from movies.serializers import MovieModelSerializer, MovieStatsSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermissions
from reviews.models import Review


class MovieLogMixin:
    def create_log(self, action, movie_id, title):
        user = self.request.user
        MovieLog.objects.create(
            action=action,
            movie_id=movie_id,
            title=title,
            user=user.username if user.is_authenticated else None,
        )


class MovieCreateListView(MovieLogMixin, generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer

    def perform_create(self, serializer):
        movie = serializer.save()
        self.create_log('create', movie.id, movie.title)


class MovieRetrieveUpdateDestroyView(MovieLogMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer

    def perform_destroy(self, instance):
        movie_id = instance.id
        instance.delete()
        self.create_log('delete', movie_id, instance.title)


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK,
        )
