"""Importance of the keys"""
default_system = {
        'views': 100,
        'likes': 50,
        'dislikes': -50,
        'comments': 50,
        'minutes_old': -1,
        }

global default_sytem

def getrecommendations(data, system=default_system):
    recommendations = {}
    for post in data:
        points = 0
        for key, value in post.items():
            if key != "name":
                points += system[key]*value
        name = post["name"]
        recommendations[name] = points


    """Copied from https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/"""
    sorted_values = sorted(recommendations.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in recommendations.keys():
            if recommendations[k] == i:
                sorted_dict[k] = recommendations[k]
                break
    """============================================================================="""
    return sorted_dict