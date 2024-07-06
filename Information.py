import csv
desired_columns = ['Rank','Game Title','Platform','Year','Genre','Publisher', 'Review']
with open('videogames.csv', 'r') as videogames_unfiltered:
    csv_reader = csv.DictReader(videogames_unfiltered)
    videogames_filtered = []
    for row in csv_reader:
        filtered_row = {key: row[key] for key in desired_columns}
        videogames_filtered.append(filtered_row)

genres = set()
platforms = set()
for game in videogames_filtered:
    genres.add(game['Genre'])
    platforms.add(game['Platform'])

platforms = list(platforms)
genres = list(genres)
