import pytest

from dao.model.movie import Movie
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None, 'Возвращается  None'
        assert type(movie) is Movie, 'Возвращается не фильм'
        assert type(movie.id) is int, 'id фильма не число'
        assert type(movie.title) is str, 'Название фильма не строка'
        assert type(movie.description) is str, 'Описание фильма не строка'
        assert type(movie.trailer) is str, 'Трейлер фильма не строка'
        assert type(movie.year) is int, 'Год выпуска фильма не число'
        assert type(movie.genre_id) is int, 'id жанра фильма не число'
        assert type(movie.director_id) is int, 'id режиссера фильма не число'

    def test_get_all(self):
        genres = self.movie_service.get_all()

        assert genres is not None, 'Возвращается  None'
        assert type(genres) is list, 'Возвращается не список'
        assert type(genres[0]) is Movie, 'Возвращается не фильм'

    def test_create(self):
        genre_data = {
            'name': 'Name_4'
        }
        genre = self.movie_service.create(genre_data)

        assert genre is not None, 'Возвращается  None'
        assert type(genre) is Movie, 'Возвращается не жанр'
        assert genre.id == 4, 'Возвращается неверный id'

    def test_update(self):
        genre_data = {
            'id': 4,
            'name': 'Name_5'
        }
        self.movie_service.update(genre_data)

    def test_delete(self):
        self.movie_service.delete(1)
