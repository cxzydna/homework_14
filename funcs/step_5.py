import sqlite3


def get_all_cast(first_actor, second_actor):
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    query = f"""
    SELECT `cast`
    FROM `netflix`
    WHERE `cast` LIKE '%{first_actor}%' 
    AND `cast` LIKE '%{second_actor}%'
    """

    cur.execute(query)
    result = cur.fetchall()
    return result


def get_actor_most_played_with(data, first_actor, second_actor):
    result = []
    set_result = {}
    for actors in data:
        result.extend(actors[0].split(', '))
        set_result = set(result)
        set_result.discard(first_actor)
        set_result.discard(second_actor)
    return list(set_result), result


def search_correct_actors(data):
    result = []
    for actor in data[0]:
        if data[1].count(actor) > 2:
            result.append(actor)
    return result


cast_ = get_all_cast("Rose McIver", "Ben Lamb")
aaa = get_actor_most_played_with(cast_, "Rose McIver", "Ben Lamb")
print(search_correct_actors(aaa))
