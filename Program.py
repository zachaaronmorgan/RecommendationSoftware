import json
with open('latest-is-20240629-001001', 'r') as file:
    data = json.load(file)

for record in data:
    print(f"Song: {record.get('title')}, Artist: {record.get('artist')}, Genre: {record.get('genre')}")