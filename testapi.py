import requests
import pandas as pd
import pprint as pp


df = pd.read_csv("sets.csv")
premiere_colonne = df[df.columns[0]].tolist()
print(premiere_colonne[:10])

key = 'f758611450c6dcd9492c00b684b4b123'

set_num = '001-1'
all_parts =[]
url = f"https://rebrickable.com/api/v3/lego/sets/{set_num}/parts/"
headers = {"Authorization": f"key {key}"}

params = {
    "page": 1,
    "page_size": 1000  # max possible
}

while True:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Ajouter les pièces de cette page
    all_parts.extend(data["results"])

    # Vérifier s’il y a une page suivante
    if data["next"] is None:
        break
    params["page"] += 1
pp.pprint(all_parts)
parts_id = []

for p in all_parts:
    parts_id.append(p["part"]["part_num"])

print(parts_id)
