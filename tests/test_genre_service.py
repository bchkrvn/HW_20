import pytest

from dao.model.genre import Genre
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None, 'Возвращается  None'
        assert type(genre) is Genre, 'Возвращается не жанр'
        assert type(genre.id) is int, 'id жанра не число'
        assert type(genre.name) is str, 'Имя жанра не строка'

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert genres is not None, 'Возвращается  None'
        assert type(genres) is list, 'Возвращается не список'
        assert type(genres[0]) is Genre, 'Возвращается не жанр'

    def test_create(self):
        genre_data = {
            'name': 'Name_4'
        }
        genre = self.genre_service.create(genre_data)

        assert genre is not None, 'Возвращается  None'
        assert type(genre) is Genre, 'Возвращается не жанр'
        assert genre.id == 4, 'Возвращается неверный id'

    def test_update(self):
        genre_data = {
            'id': 4,
            'name': 'Name_5'
        }
        self.genre_service.update(genre_data)

    def test_delete(self):
        self.genre_service.delete(1)
