import pandas as pd

# print(date[-4:])
# name, platform, r-date, score, genre, players
games = pd.read_csv('games-data.csv')
video_games = []
for index,game in games.iterrows():
    video_games.append(game)

platforms = set()
genres = set()

for game in video_games:
    game['r-date'] = game['r-date'][-4:]
    for genre in game['genre'].split(','):
        genres.add(genre.strip())
    platforms.add(game['platform'])
    # platforms.add(game['platform'])
    # genres.add(game['genre'])

# platforms = list(platforms)
# genres = list(genres)

# print(platforms,'\n')
# print(genres)
platforms = list(platforms)
genres = list(genres)

platforms = sorted(platforms)
genres = sorted(genres)
