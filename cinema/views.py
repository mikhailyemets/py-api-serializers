from rest_framework import viewsets
from cinema.models import Movie, Actor, Genre, CinemaHall, MovieSession
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

