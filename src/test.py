import main

data = [
    {'name': 'best', 'views': 10000, 'likes': 1000, 'dislikes': 10, 'comments': 100, 'minutes_old': 24*60},
    {'name': 'good', 'views': 5000, 'likes': 500, 'dislikes': 5, 'comments': 50, 'minutes_old': 24*60},
    {'name': 'trending', 'views': 2000, 'likes': 200, 'dislikes': 2, 'comments': 20, 'minutes_old': 4*60},
    {'name': 'new', 'views': 1000, 'likes': 100, 'dislikes': 1, 'comments': 10, 'minutes_old': 2*60},
    {'name': 'average', 'views': 1000, 'likes': 100, 'dislikes': 1, 'comments': 20, 'minutes_old': 48*60},
    {'name': 'old', 'views': 5000, 'likes': 500, 'dislikes': 5, 'comments': 50, 'minutes_old': 7*24*60},
    {'name': 'controversial', 'views': 2000, 'likes': 100, 'dislikes': 50, 'comments': 50, 'minutes_old': 32*60},
    {'name': 'bad', 'views': 750, 'likes': 7, 'dislikes': 1, 'comments': 3, 'minutes_old': 24*60},
]

print(main.getrecommendations(data))