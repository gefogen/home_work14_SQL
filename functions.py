import sqlite3


def connect_db():
    """ Устанавливаем соединение с БД """
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        conn = conn.cursor()
    return conn


def search_by_name(title):
    """ Поиск фильма по названию """
    db = connect_db()
    db.execute("SELECT title, country, release_year, listed_in, description "
               "FROM netflix "
               "WHERE title != '' "
               "ORDER BY release_year DESC ")

    get_film = []

    for film in db:
        if str(title).lower() in film['title'].lower():
            get_film.append(dict(film))

    return get_film


def search_by_years(year, years):
    """ Поиск фильмов по годам """
    db = connect_db()
    sql = f""" SELECT title, release_year
                FROM netflix 
                WHERE release_year BETWEEN {year} AND {years}
                ORDER BY release_year DESC
                LIMIT 100
        """
    db.execute(sql)

    get_film = []

    for film in db:
        get_film.append(dict(film))

    return get_film


def search_by_rating_children():
    """ Поиск фильмов для детей """
    db = connect_db()
    sql = f""" SELECT title, rating, description
                    FROM netflix 
                    WHERE rating == 'G'
            """
    db.execute(sql)

    get_film = []

    for film in db:
        get_film.append(dict(film))

    return get_film


def search_by_rating_family():
    """ Поиск фильмов для семьи """
    db = connect_db()
    sql = f""" SELECT title, rating, description
                FROM netflix 
                WHERE rating == 'G'
                OR rating == 'PG'
                OR rating == 'PG-13'
            """
    db.execute(sql)

    get_film = []

    for film in db:
        get_film.append(dict(film))

    return get_film


def search_by_rating_adult():
    """ Поиск фильмов для взрослых """
    db = connect_db()
    sql = f""" SELECT title, rating, description
                    FROM netflix 
                    WHERE rating == 'R'
                    OR rating == 'NC-17'
                """
    db.execute(sql)

    get_film = []

    for film in db:
        get_film.append(dict(film))

    return get_film


def search_by_genre(genre):
    """ Поиск фильмов по жанру """
    db = connect_db()
    sql = f""" SELECT title, description, listed_in
                FROM netflix 
            """
    db.execute(sql)

    get_film = []

    for film in db:
        genres = film['listed_in']
        if str(genre).lower() in genres.lower():
            get_film.append(dict(film))

    return get_film


def get_cast(actor, actors):
    """ Поиск актёров """
    db = connect_db()
    sql = f""" SELECT netflix.cast
                FROM netflix 
                """
    db.execute(sql)

    get_actors = []

    for film in db:
        list_actors = film['cast']
        if actor.lower() and actors.lower() in list_actors.lower():
            get_actors.append(list_actors)

    return get_actors


def get_paint(type, release_year, listed_in):
    """ Поиск названий картин и их описаний  """
    db = connect_db()
    sql = f""" SELECT *
                FROM netflix
                WHERE release_year == {release_year} 
                """
    db.execute(sql)

    get_film = []

    for film in db:
        genres = film['listed_in']
        type_of_film = film['type']
        if str(listed_in).lower() in genres.lower() and str(type).lower() in type_of_film.lower():
            corect = {
                "title": film['title'],
                "description": film['description']
            }
            get_film.append(dict(corect))

    return get_film
