from flask import Blueprint, jsonify

from rating_bp import utils, queries

rating_bp = Blueprint("rating_bp", __name__)


@rating_bp.route('/<group>')
def movie_by_group_page(group):
    rating = utils.get_rating(group)
    query = queries.get_movie_by_rating_query(rating)
    data = utils.get_movie_by_rating(query)
    result = utils.get_movie_by_rating_to_dict(data)
    return jsonify(result)
