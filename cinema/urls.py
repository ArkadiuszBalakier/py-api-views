from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, CinemaHallViewSet, GenreListView, GenreDetailView

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'cinema_halls', CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
]

app_name = "cinema"
