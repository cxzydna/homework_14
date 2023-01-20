def get_movie_by_rating_query(rating):
    query = f"""
        SELECT `title`, `rating`, `description`
        FROM netflix
        WHERE `rating` IN {rating}
        AND `type` = 'Movie'
        """

    return query
