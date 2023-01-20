def movie_by_genre_query(genre):
    query = f"""
        SELECT `title`, `description`
        FROM `netflix`
        WHERE listed_in LIKE '%{genre}%'
        AND `type` = 'Movie'
        ORDER BY `release_year` DESC 
        LIMIT 10
        """

    return query
