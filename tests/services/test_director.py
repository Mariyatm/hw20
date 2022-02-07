from unittest.mock import MagicMock
import pytest
from dao.model.director import Director
from service.director import DirectorService, DirectorDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director1 = Director(id=1, name="Квентин Тарантино")
    director2 = Director(id=2, name="Стэнли Кубрик")
    director_dao.get_one = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=[director1, director2])
    director_dao.create = MagicMock(return_value=director2)
    director_dao.update = MagicMock(return_value=director2)
    director_dao.delete = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None
        assert isinstance(director.name, str)

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_data = {"id": 1, "name": "director"}
        director = self.director_service.create(director_data)

        assert director is not None

    def test_update(self):
        director_data = {"id": 1, "name": "director"}
        director = self.director_service.update(director_data)

        assert director is not None

    def test_partially_update(self):
        director_data = {"id": 1, "name": "director"}
        director = self.director_service.partially_update(director_data)

    def test_delete(self):
        self.director_service.delete(1)
