from flask import Blueprint, jsonify

from movies_bp import utils, queries

movies_bp = Blueprint("movies_bp", __name__)


@movies_bp.route('/<title>')
def movie_page(title):
    query = queries.get_movie_by_title_query(title)
    data = utils.get_movie_by_title(query)
    result = utils.get_movie_by_title_to_dict(data)
    return jsonify(result)


@movies_bp.route('/<int:from_year>/to/<int:to_year>')
def movies_page(from_year, to_year):
    query = queries.get_movie_by_year_query(from_year, to_year)
    data = utils.get_movie_by_year(query)
    result = utils.get_movie_by_year_to_dict(data)
    return jsonify(result)
