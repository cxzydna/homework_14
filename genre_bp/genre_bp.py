from flask import Blueprint, jsonify

from genre_bp import utils, queries

genre_bp = Blueprint("genre_bp", __name__)


@genre_bp.route('/<genre>')
def movie_by_genre_page(genre):
    query = queries.movie_by_genre_query(genre)
    data = utils.get_movie_by_genre(query)
    result = utils.get_movie_by_genre_to_dict(data)
    return jsonify(result)
