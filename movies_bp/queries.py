def get_movie_by_title_query(title):
    query = f"""
        SELECT `title`, `country`, `release_year`, `listed_in`, `description`
        FROM `netflix`
        WHERE `title` = {title} AND `type` = 'Movie'
        ORDER BY `release_year` DESC 
        LIMIT 1
        """
    return query


def get_movie_by_year_query(from_year, to_year):
    query = f"""
        SELECT `title`, `release_year`
        FROM `netflix` 
        WHERE `release_year` BETWEEN {from_year} AND {to_year}
        AND `type` = 'Movie'
        LIMIT 100
        """
    return query