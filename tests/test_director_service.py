import pytest

from dao.model.director import Director
from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None, 'Возвращается  None'
        assert type(director) is Director, 'Возвращается не режиссер'
        assert type(director.id) is int, 'id режиссера не число'
        assert type(director.name) is str, 'Имя режиссера не строка'

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None, 'Возвращается  None'
        assert type(directors) is list, 'Возвращается не список'
        assert type(directors[0]) is Director, 'Возвращается не режиссер'

    def test_create(self):
        director_data = {
            'name': 'Name_4'
        }
        director = self.director_service.create(director_data)

        assert director is not None, 'Возвращается  None'
        assert type(director) is Director, 'Возвращается не режиссер'
        assert director.id == 4, 'Возвращается неверный id'

    def test_update(self):
        director_data = {
            'id': 4,
            'name': 'Name_5'
        }
        self.director_service.update(director_data)

    def test_delete(self):
        self.director_service.delete(1)
