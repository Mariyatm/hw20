from unittest.mock import MagicMock
import pytest
from dao.model.genre import Genre
from service.genre import GenreService, GenreDAO


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre1 = Genre(id=1, name="триллер")
    genre2 = Genre(id=2, name="комедия")
    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2])
    genre_dao.create = MagicMock(return_value=genre2)
    genre_dao.update = MagicMock(return_value=genre2)
    genre_dao.delete = MagicMock()
    return genre_dao


class TestgenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None
        assert isinstance(genre.name, str)

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        genre_data = {"id": 1, "name": "genre"}
        genre = self.genre_service.create(genre_data)

        assert genre is not None

    def test_update(self):
        genre_data = {"id": 1, "name": "genre"}
        genre = self.genre_service.update(genre_data)

        assert genre is not None

    def test_partially_update(self):
        genre_data = {"id": 1, "name": "genre"}
        genre = self.genre_service.partially_update(genre_data)

    def test_delete(self):
        self.genre_service.delete(1)
