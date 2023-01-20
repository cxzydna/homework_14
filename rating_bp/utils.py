import sqlite3


def get_rating(group):
    """
    The function returns ratings based on the passed group
    :param group:  - a group of spectators
    :return:       - ratings
    """
    if group.lower() == "children":
        return "G"
    elif group.lower() == "family":
        return 'G', 'PG', 'PG-13'
    elif group.lower() == "adult":
        return 'R', 'NC-17'
    else:
        return 'Dont know this group'


def get_movie_by_rating(query):
    """
    The function performs work with the database
    :param query:  - sql query
    :return:       - list of results
    """
    con = sqlite3.connect("netflix.db")
    cursor = con.cursor()

    cursor.execute(query)
    data = cursor.fetchall()
    con.close()

    return data


def get_movie_by_rating_to_dict(data):
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
                "rating": movie[1].strip("\n"),
                "description": movie[2].strip("\n")
            }
            result.append(my_dict)
    except IndexError:
        result = []
    return result
