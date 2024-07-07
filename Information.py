import pandas as pd

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

platforms = list(platforms)
genres = list(genres)

platforms = sorted(platforms)
genres = sorted(genres)


# Video games format: name, platform, r-date, score,  user score, developer, genre, players, critics, users
print(video_games[0])