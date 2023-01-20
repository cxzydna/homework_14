import sqlite3


def get_movie_by_genre(query):
    """
    The function performs work with the database
    :param query: - sql query
    :return:      - list of results
    """
    con = sqlite3.connect("netflix.db")
    cursor = con.cursor()

    cursor.execute(query)
    data = cursor.fetchall()
    con.close()

    return data


def get_movie_by_genre_to_dict(data):
    """
    The function translates the data into a dictionary format
    :param data:  - movies
    :return:      dict of movies
    """
    result = []
    try:
        for movie in data:
            my_dict = {
                "title": movie[0].strip("\n"),
                "description": movie[1].strip("\n")
            }
            result.append(my_dict)
    except IndexError:
        result = []
    return result
