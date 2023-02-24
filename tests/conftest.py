from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


@pytest.fixture
def director_dao():
    d_1 = Director(id=1, name='Name_1')
    d_2 = Director(id=2, name='Name_2')
    d_3 = Director(id=3, name='Name_3')
    d_list = [d_1, d_2, d_3]

    director_dao = DirectorDAO(None)
    director_dao.get_one = MagicMock(return_value=d_1)
    director_dao.get_all = MagicMock(return_value=d_list)
    director_dao.create = MagicMock(return_value=Director(id=4, name='Name_4'))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao():
    g_1 = Genre(id=1, name='Name_1')
    g_2 = Genre(id=2, name='Name_2')
    g_3 = Genre(id=3, name='Name_3')
    g_list = [g_1, g_2, g_3]

    genre_dao = GenreDAO(None)
    genre_dao.get_one = MagicMock(return_value=g_1)
    genre_dao.get_all = MagicMock(return_value=g_list)
    genre_dao.create = MagicMock(return_value=Genre(id=4, name='Name_4'))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture
def movie_dao():
    m_1 = Movie(id=1,
                title='Title_1',
                description='description_1',
                trailer='trailer_1',
                year=1,
                genre_id=1,
                director_id=1)

    m_2 = Movie(id=2,
                title='Title_2',
                description='description_2',
                trailer='trailer_2',
                year=2,
                genre_id=2,
                director_id=2)

    m_3 = Movie(id=3,
                title='Title_3',
                description='description_3',
                trailer='trailer_3',
                year=3,
                genre_id=3,
                director_id=3)

    m_list = [m_1, m_2, m_3]
    movie_dao = GenreDAO(None)
    movie_dao.get_one = MagicMock(return_value=m_1)
    movie_dao.get_all = MagicMock(return_value=m_list)
    movie_dao.create = MagicMock(return_value=Movie(id=4,
                                                    title='Title_4',
                                                    description='description_4',
                                                    trailer='trailer_4',
                                                    year=4,
                                                    genre_id=4,
                                                    director_id=4
                                                    ))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
