import sqlite3


def get_movie_by_title(query):
    """
    The function performs work with the database
    :param query:  - sql query
    :return:       - movie
    """
    con = sqlite3.connect("netflix.db")
    cursor = con.cursor()

    cursor.execute(query)
    data = cursor.fetchall()
    con.close()

    return data


def get_movie_by_title_to_dict(data):
    """
    The function translates the data into a dictionary format
    :param data:  - movies
    :return:      dict of movies
    """
    try:
        result = []
        for movie in data:
            my_dict = {
                "title": movie[0].strip("\n"),
                "country": movie[1].strip("\n"),
                "release_year": str(movie[2]).strip("\n"),
                "genre": movie[3].strip("\n"),
                "description": movie[4].strip("\n"),
            }
            result.append(my_dict)

        return result[0]
    except IndexError:
        return []


def get_movie_by_year(query):
    """
    The function performs work with the database
    :param query:  - sql query
    :return:       - movie
    """
    con = sqlite3.connect("netflix.db")
    cursor = con.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    con.close()
    return data


def get_movie_by_year_to_dict(data):
    """
    The function translates the data into a dictionary format
    :param data:  - movies
    :return:      dict of movies
    """
    result = []
    for movie in data:
        my_dict = {
            "title": movie[0],
            "release_year": movie[1]
        }
        result.append(my_dict)
    return result
