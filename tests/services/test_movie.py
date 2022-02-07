from unittest.mock import MagicMock
import pytest
from dao.model.movie import Movie
from service.movie import MovieService, MovieDAO


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie1 = Movie(id=1, title="Омерзительная восьмёрка")
    movie2 = Movie(id=2, title="Сияние")
    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2])
    movie_dao.create = MagicMock(return_value=movie2)
    movie_dao.update = MagicMock(return_value=movie2)
    movie_dao.delete = MagicMock()
    return movie_dao


class TestmovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None
        assert isinstance(movie.name, str)

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_data = {"id": 1, "name": "movie"}
        movie = self.movie_service.create(movie_data)

        assert movie is not None

    def test_update(self):
        movie_data = {"id": 1, "name": "movie"}
        movie = self.movie_service.update(movie_data)

        assert movie is not None

    def test_partially_update(self):
        movie_data = {"id": 1, "description": "труляля"}
        movie = self.movie_service.partially_update(movie_data)

    def test_delete(self):
        self.movie_service.delete(1)
