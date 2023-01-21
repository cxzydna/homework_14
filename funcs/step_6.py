import sqlite3
import json


def get_movies(type_of_movie, year, genre):
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    query = f"""
    SELECT `title`, `description`
    FROM `netflix`
    WHERE `type` = '{type_of_movie.title()}'
    AND `release_year` = '{year}'
    AND `listed_in` LIKE '%{genre}%'
    """
    cur.execute(query)
    data = cur.fetchall()
    return data


def movie_to_dict(data):
    result = []
    for movie in data:
        my_dict = {
            "title": movie[0].strip("\n"),
            "description": movie[1].strip("\n")
        }
        result.append(my_dict)
    return result


def movie_to_json(data):
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(data, f)
    return 'Данные загружены'


movies = get_movies('movie', '1990', 'dramas')
movie_dict = movie_to_dict(movies)
print(movie_to_json(movie_dict))
