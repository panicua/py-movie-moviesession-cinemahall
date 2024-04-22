import datetime

from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime, *,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.get_or_create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    all_movie_sessions = MovieSession.objects.all()
    if session_date is not None:
        return all_movie_sessions.filter(show_time__date=session_date)
    return all_movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int, *,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:
    if all(
            argument is None
            for argument in (show_time, movie_id, cinema_hall_id)
    ):
        return

    session_to_update = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        session_to_update.show_time = show_time
    if movie_id is not None:
        session_to_update.movie_id = movie_id
    if cinema_hall_id is not None:
        session_to_update.cinema_hall_id = cinema_hall_id

    session_to_update.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
